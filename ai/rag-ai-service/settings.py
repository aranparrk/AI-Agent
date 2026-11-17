from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Spring과 동일한 타입으로 지정
    service_token: str

    rag_engine = str = "stub"

    # 청크 분할
    chunk_size: int = 500
    chunk_overlap: int = 8

    # 근거로 인정하는 최소 점수
    stub_min_score: float = 0.3  # 2-gram 겹침 비율 (0~1)
    min_score: float = 0.78  # Atlas 코사인 점수 (0~1 로 변환된 값)

    # OpenAI (atlas 엔진에서만 사용)
    openai_api_key: str = ""
    openai_embedding_model: str = "text-embedding-3-small"
    openai_chat_model: str = "gpt-4.1-mini"
    embedding_dimensions: int = 1536

    # MongoDB Atlas (atlas 엔진에서만 사용)
    mongodb_uri: str = ""
    mongodb_db: str = "rag"
    mongodb_collection: str = "board_chunks"
    atlas_index_name: str = "board_vector_index"