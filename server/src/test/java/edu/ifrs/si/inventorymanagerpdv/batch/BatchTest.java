package edu.ifrs.si.inventorymanagerpdv.batch;

import static org.assertj.core.api.Assertions.assertThat;

import java.net.URI;
import java.time.LocalDateTime;

import edu.ifrs.si.inventorymanagerpdv.model.Batch;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.HttpMethod;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import com.jayway.jsonpath.DocumentContext;
import com.jayway.jsonpath.JsonPath;
import org.springframework.test.annotation.DirtiesContext;


@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class BatchTest {

    @Autowired
    TestRestTemplate restTemplate;


    @Test
    void shouldReturnABatchWhenDataExists() {
        ResponseEntity<String> response = restTemplate.getForEntity("/batches?product=1", String.class);
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);

        DocumentContext documentContext = JsonPath.parse(response.getBody());
        Number id = documentContext.read("$[0].id");
        String batchId = documentContext.read("$[0].batchId");
        Number productId = documentContext.read("$[0].product.id");
        String productName = documentContext.read("$[0].product.name");
        Double cost = documentContext.read("$[0].cost");
        Number quantity = documentContext.read("$[0].quantity");
        LocalDateTime validationDate = LocalDateTime.parse(documentContext.read("$[0].validationDate"));
        LocalDateTime createdAt = LocalDateTime.parse(documentContext.read("$[0].createdAt"));
        LocalDateTime updatedAt = LocalDateTime.parse(documentContext.read("$[0].updatedAt"));

        assertThat(id).isEqualTo(1);
        assertThat(batchId).isEqualTo("123ABC456");
        assertThat(productId).isEqualTo(1);
        assertThat(productName).isEqualTo("Fandangos");
        assertThat(cost).isEqualTo(200.00);
        assertThat(quantity).isEqualTo(350);
        assertThat(validationDate).isEqualTo("2023-10-01T10:00:00");
        assertThat(createdAt).isEqualTo("2023-10-01T10:00:00");
        assertThat(updatedAt).isEqualTo("2023-10-01T10:00:00");
    }


    @Test
    void shouldNotReturnAnyBatchesWithAnUnknownProductId() {
        ResponseEntity<String> response = restTemplate
                .getForEntity("/batches?product=2421", String.class);

        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.NOT_FOUND);
        assertThat(response.getBody()).isBlank();
    }


    @Test
    @DirtiesContext
    void shouldCreateAKnewBatchWhenProductExists() {
        Batch batch = new Batch(null, "34456GBVX", 4L, 400.00, 100, LocalDateTime.parse("2025-11-19T09:00:00"), LocalDateTime.parse("2025-11-19T10:00:00"), LocalDateTime.parse("2025-11-19T11:00:00"));

        ResponseEntity<Void> createResponse = restTemplate.postForEntity("/batches", batch, Void.class);
        assertThat(createResponse.getStatusCode()).isEqualTo(HttpStatus.CREATED);

        URI locationOfNewBatch = createResponse.getHeaders().getLocation();
        ResponseEntity<String> getResponse = restTemplate.getForEntity(locationOfNewBatch, String.class);
        assertThat(getResponse.getStatusCode()).isEqualTo(HttpStatus.OK);

        DocumentContext documentContext = JsonPath.parse(getResponse.getBody());
        Number id = documentContext.read("$.id");
        assertThat(id).isNotNull();
        String batchId = documentContext.read("$.batchId");
        assertThat(batchId).isEqualTo("34456GBVX");
        Number productId = documentContext.read("$.product.id");
        assertThat(productId).isEqualTo(4);
        String productName = documentContext.read("$.product.name");
        assertThat(productName).isEqualTo("Guaraná Antarctica 2L");
        Double cost = documentContext.read("$.cost");
        assertThat(cost).isEqualTo(400.00);
        Number quantity = documentContext.read("$.quantity");
        assertThat(quantity).isEqualTo(100);
        String validationDate = documentContext.read("$.validationDate");
        assertThat(LocalDateTime.parse(validationDate)).isEqualTo("2025-11-19T09:00:00");
        String createdAt = documentContext.read("$.createdAt");
        assertThat(createdAt).isEqualTo("2025-11-19T10:00:00");
        String updatedAt = documentContext.read("$.updatedAt");
        assertThat(updatedAt).isEqualTo("2025-11-19T11:00:00");
    }


    @Test
    @DirtiesContext
    void shouldConsumeInventoryWhenSufficientQuantityExists() {
        ResponseEntity<Integer> response = restTemplate.exchange(
                "/batches/consume/1?quantity=351",
                HttpMethod.PATCH,
                null, Integer.class
        );
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
    }
}
