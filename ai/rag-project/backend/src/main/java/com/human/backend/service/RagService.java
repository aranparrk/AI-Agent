package com.human.backend.service;

import com.human.backend.dto.RagQuestion;

import java.net.http.HttpClient;
import java.time.Duration;
import java.util.Map;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.http.client.JdkClientHttpRequestFactory;
import org.springframework.web.client.ResourceAccessException;
import org.springframework.web.client.RestClient;
import org.springframework.web.client.RestClientResponseException;
import org.springframework.stereotype.Service;

@Service
public class RagService {
    private final RestClient aiClient;

    public RagService(@Value("${rag.ai-base-url}") String baseUrl) {
        HttpClient httpClient = HttpClient.newBuilder()
                .version(HttpClient.Version.HTTP_1_1)
                .connectTimeout(Duration.ofSeconds(3))
                .build();
        JdkClientHttpRequestFactory requestFactory = new JdkClientHttpRequestFactory(httpClient);
        requestFactory.setReadTimeout(Duration.ofSeconds(35));
        aiClient = RestClient.builder()
                .baseUrl(baseUrl)
                .requestFactory(requestFactory)
                .build();
    }

    public ResponseEntity<?> meta() {
        return forward(aiClient.get().uri("/api/meta"));
    }

    public ResponseEntity<?> ask(RagQuestion request) {
        return forward(aiClient.post().uri("/api/ask")
                .contentType(MediaType.APPLICATION_JSON)
                .body(request));
    }

    private ResponseEntity<?> forward(RestClient.RequestHeadersSpec<?> request) {
        try {
            return request.retrieve().toEntity(Map.class);
        } catch (RestClientResponseException error) {
            if (error.getStatusCode().is4xxClientError()) {
                return ResponseEntity.status(error.getStatusCode())
                        .contentType(MediaType.APPLICATION_JSON)
                        .body(error.getResponseBodyAsString());
            }
            return ResponseEntity.status(502).body(Map.of("detail", "AI 서비스 요청 처리에 실패했어요."));
        } catch (ResourceAccessException error) {
            return ResponseEntity.status(503).body(Map.of("detail", "AI 서비스에 연결할 수 없어요."));
        }
    }
}
