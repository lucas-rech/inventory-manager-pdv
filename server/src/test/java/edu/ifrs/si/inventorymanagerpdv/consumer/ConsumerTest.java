package edu.ifrs.si.inventorymanagerpdv.consumer;

import com.jayway.jsonpath.DocumentContext;
import com.jayway.jsonpath.JsonPath;
import edu.ifrs.si.inventorymanagerpdv.model.dto.CreateConsumerDTO;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class ConsumerTest {

    @Autowired
    TestRestTemplate restTemplate;

    @Test
    void shouldReturnAllConsumersWhenDataExists() {
        ResponseEntity<String> response = restTemplate
            .getForEntity("/consumers", String.class);
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);

        DocumentContext documentContext = JsonPath.parse(response.getBody());
        Number id = documentContext.read("$.[0].id");
        assertThat(id).isEqualTo(1);
        String name = documentContext.read("$.[0].name");
        assertThat(name).isEqualTo("Alex");
        String lastName = documentContext.read("$.[0].lastName");
        assertThat(lastName).isEqualTo("Turner");
        String email = documentContext.read("$.[0].email");
        assertThat(email).isEqualTo("alexturner@gmail.com");
        String document = documentContext.read("$.[0].document");
        assertThat(document).isEqualTo("94387634945");
        String phoneNumber = documentContext.read("$.[0].phoneNumber");
        assertThat(phoneNumber).isEqualTo("54999998888");
        String createdAt = documentContext.read("$.[0].createdAt");
        assertThat(createdAt).isEqualTo("2024-05-20T14:30:00");
        String updatedAt = documentContext.read("$.[0].updatedAt");
        assertThat(updatedAt).isEqualTo("2024-05-20T14:30:00");
    }


    @Test
    void shouldReturnAConsumerWhenIdExists() {
        ResponseEntity<String> response = restTemplate
            .getForEntity("/consumers/1", String.class);
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);

        DocumentContext documentContext = JsonPath.parse(response.getBody());
        Number id = documentContext.read("$.id");
        assertThat(id).isEqualTo(1);
        String name = documentContext.read("$.name");
        assertThat(name).isEqualTo("Alex");
        String lastName = documentContext.read("$.lastName");
        assertThat(lastName).isEqualTo("Turner");
        String email = documentContext.read("$.email");
        assertThat(email).isEqualTo("alexturner@gmail.com");
        String document = documentContext.read("$.document");
        assertThat(document).isEqualTo("94387634945");
        String phoneNumber = documentContext.read("$.phoneNumber");
        assertThat(phoneNumber).isEqualTo("54999998888");
        String createdAt = documentContext.read("$.createdAt");
        assertThat(createdAt).isEqualTo("2024-05-20T14:30:00");
        String updatedAt = documentContext.read("$.updatedAt");
        assertThat(updatedAt).isEqualTo("2024-05-20T14:30:00");
    }


    @Test
    void shouldNotReturnAConsumerWhenIdDoesNotExist() {
        ResponseEntity<String> response = restTemplate
            .getForEntity("/consumers/999", String.class);
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.NOT_FOUND);
    }


    @Test
    void shouldCreateANewConsumer() {
        CreateConsumerDTO newConsumer = new CreateConsumerDTO(
                "Jamie",
                "Cook",
                "jamiecook@gmail.com",
                "12345678900",
                "54988887777");

        ResponseEntity<Void> response = restTemplate
                .postForEntity("/consumers", newConsumer, Void.class);
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.CREATED);
    }
}
