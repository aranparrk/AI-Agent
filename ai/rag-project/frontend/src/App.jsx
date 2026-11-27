import { useEffect, useRef, useState } from 'react'
import Markdown from 'react-markdown'
import './App.css'

const examples = [
  { label: 'React 상태 업데이트', question: 'React에서 이전 상태를 바탕으로 값을 업데이트하려면 어떻게 해?' },
  { label: 'useEffect 정리 함수', question: 'useEffect가 반환하는 정리 함수는 언제 실행돼?' },
  { label: 'FastAPI 요청 본문', question: 'FastAPI에서 JSON 요청 본문을 Pydantic 모델로 받으려면?' },
  { label: 'FastAPI CORS 설정', question: 'React에서 FastAPI로 요청할 때 CORS를 어떻게 설정해?' },
]

function AnswerText({ answer, sources }) {
  const citations = sources.map(({ number }) => `[${number}]`).join(' ')
  const hasCitations = citations && answer.endsWith(' ' + citations)
  const text = hasCitations ? answer.slice(0, -citations.length).trimEnd() : answer

  return (
    <div className="answer-text">
      <Markdown skipHtml disallowedElements={['a', 'img']} unwrapDisallowed>{text}</Markdown>
      {hasCitations && sources.map(({ number }) => (
        <a key={number} href={'#source-' + number} className="citation" aria-label={'근거 ' + number + '번'}>
          {number}
        </a>
      ))}
    </div>
  )
}

function App() {
  const [question, setQuestion] = useState('')
  const [meta, setMeta] = useState(null)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const input = useRef(null)

  useEffect(() => {
    const controller = new AbortController()

    fetch('/api/meta', { signal: controller.signal })
      .then((response) => (response.ok ? response.json() : null))
      .then(setMeta)
      .catch(() => {})

    return () => controller.abort()
  }, [])

  function selectExample(example) {
    setQuestion(example)
    input.current?.focus()
  }

  async function ask(event) {
    event.preventDefault()
    const text = question.trim()
    if (!text || loading) return

    setError('')
    setResult(null)
    setLoading(true)
    try {
      const response = await fetch('/api/ask', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: text }),
        signal: AbortSignal.timeout(40000),
      })
      if (!response.ok) {
        if (response.status === 502 || response.status === 503) {
          throw new Error('AI 서비스에 연결할 수 없어요. 서버가 실행 중인지 확인해 주세요.')
        }
        throw new Error('질문을 처리하지 못했어요. 잠시 후 다시 시도해 주세요.')
      }
      setResult(await response.json())
    } catch (requestError) {
      const message = requestError.name === 'TimeoutError'
        ? '응답 시간이 초과됐어요. 다시 질문해 주세요.'
        : requestError instanceof TypeError
          ? '서버에 연결할 수 없어요. 연결 상태를 확인해 주세요.'
          : requestError.message
      setError(message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="site">
      <header className="topbar">
        <div className="shell header-inner">
          <div className="brand"><span className="brand-mark" aria-hidden="true">&gt;_</span> 개발 문서 Q&amp;A</div>
          <a className="header-link" href="https://ko.react.dev/learn" target="_blank" rel="noreferrer">
            React 공식 문서 <span aria-hidden="true">↗</span>
          </a>
        </div>
      </header>

      <main className="shell">
        <section className="intro" aria-labelledby="page-title">
          <h1 id="page-title">개발 문서에 물어보세요</h1>
          <p>React와 FastAPI 공식 문서에서 관련 내용을 찾아 출처와 함께 답변해요.</p>
        </section>

        <div className="layout">
          <div className="main-column">
            <form className="question-panel" onSubmit={ask}>
              <label htmlFor="question">어떤 게 궁금하세요?</label>
              <textarea
                id="question"
                ref={input}
                value={question}
                maxLength={500}
                rows={3}
                placeholder="예: FastAPI에서 경로 매개변수를 정수로 검증하려면?"
                onChange={(event) => setQuestion(event.target.value)}
              />
              <div className="form-footer">
                <span className="character-count">{question.length} / 500</span>
                <button className="ask-button" type="submit" disabled={!question.trim() || loading}>
                  {loading ? '검색 중…' : '질문하기'} <span aria-hidden="true">→</span>
                </button>
              </div>
            </form>

            <div className="result-area" aria-live="polite" aria-busy={loading}>
              {loading && <p className="notice"><span className="spinner" aria-hidden="true" /> 관련 문서를 검색하고 있어요.</p>}
              {error && <p className="notice error" role="alert">{error}</p>}
              {result && (
                <section className="response" aria-labelledby="answer-title">
                  <h2 id="answer-title">{result.mode === 'evidence_only' ? '검색 결과' : '답변'}</h2>
                  <AnswerText answer={result.answer} sources={result.sources} />
                  {result.sources.length > 0 && (
                    <>
                      <h3>출처</h3>
                      <ol className="sources">
                        {result.sources.map((source) => (
                          <li className="source" key={source.document_id} id={'source-' + source.number}>
                            <div className="source-heading">
                              <span className="source-number" aria-label={'근거 ' + source.number + '번'}>{source.number}</span>
                              <div>
                                <a href={source.url} target="_blank" rel="noreferrer">
                                  {source.title} <span aria-hidden="true">↗</span>
                                </a>
                                <p>{source.technology} · {source.heading}</p>
                              </div>
                            </div>
                            <div className="excerpt">
                              <Markdown skipHtml disallowedElements={['a', 'img']} unwrapDisallowed>{source.excerpt}</Markdown>
                            </div>
                          </li>
                        ))}
                      </ol>
                    </>
                  )}
                </section>
              )}
            </div>
          </div>

          <aside className="reference">
            <section aria-labelledby="examples-title">
              <h2 id="examples-title">이렇게 물어보세요</h2>
              <ul className="examples">
                {examples.map((example) => (
                  <li key={example.label}>
                    <button type="button" onClick={() => selectExample(example.question)}>
                      {example.label} <span aria-hidden="true">↗</span>
                    </button>
                  </li>
                ))}
              </ul>
            </section>
            {meta && (
              <section className="scope" aria-labelledby="scope-title">
                <h2 id="scope-title">검색 범위</h2>
                <p>React 상태·훅, FastAPI 요청·응답·의존성·CORS</p>
                <p>공식 문서 {meta.documents}개 · 청크 {meta.chunks}개</p>
                {!meta.generationAvailable && <p className="mode">현재 근거 검색 모드</p>}
              </section>
            )}
          </aside>
        </div>
      </main>
    </div>
  )
}

export default App
