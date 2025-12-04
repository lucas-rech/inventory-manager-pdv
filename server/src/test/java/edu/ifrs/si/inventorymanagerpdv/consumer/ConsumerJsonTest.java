package edu.ifrs.si.inventorymanagerpdv.consumer;


import edu.ifrs.si.inventorymanagerpdv.model.Consumer;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.json.JsonTest;
import org.springframework.boot.test.json.JacksonTester;

import java.time.LocalDateTime;

import static org.assertj.core.api.Assertions.assertThat;


@JsonTest
public class ConsumerJsonTest {

    @Autowired
    private JacksonTester<Consumer> json;


    @Test
    void consumerSerializeTest() throws Exception {
        Consumer consumer = new Consumer(
                40L,
                "Alex",
                "Turner",
                "alexturner@gmail.com",
                "94387634945",
                "54999998888",
                LocalDateTime.parse("2024-05-20T14:30:00"),
                LocalDateTime.parse("2024-05-20T14:30:00")
        );

        assertThat(json.write(consumer)).isStrictlyEqualToJson("single-consumer.json");
        assertThat(json.write(consumer)).hasJsonPathNumberValue("@.id");
        assertThat(json.write(consumer)).extractingJsonPathNumberValue("@.id").isEqualTo(40);
        assertThat(json.write(consumer)).hasJsonPathStringValue("@.name");
        assertThat(json.write(consumer)).extractingJsonPathStringValue("@.name").isEqualTo("Alex");
        assertThat(json.write(consumer)).hasJsonPathStringValue("@.lastName");
        assertThat(json.write(consumer)).extractingJsonPathStringValue("@.lastName").isEqualTo("Turner");
        assertThat(json.write(consumer)).hasJsonPathStringValue("@.email");
        assertThat(json.write(consumer)).extractingJsonPathStringValue("@.email").isEqualTo("alexturner@gmail.com");
        assertThat(json.write(consumer)).hasJsonPathStringValue("@.document");
        assertThat(json.write(consumer)).extractingJsonPathStringValue("@.document").isEqualTo("94387634945");
        assertThat(json.write(consumer)).hasJsonPathStringValue("@.phoneNumber");
        assertThat(json.write(consumer)).extractingJsonPathStringValue("@.phoneNumber").isEqualTo("54999998888");
        assertThat(json.write(consumer)).hasJsonPathStringValue("@.createdAt");
        assertThat(json.write(consumer)).extractingJsonPathStringValue("@.createdAt").isEqualTo("2024-05-20T14:30:00");
        assertThat(json.write(consumer)).hasJsonPathStringValue("@.updatedAt");
        assertThat(json.write(consumer)).extractingJsonPathStringValue("@.updatedAt").isEqualTo("2024-05-20T14:30:00");
    }



    @Test
    void consumerDeserializeTest() throws Exception {
        String expected = """
                {
                      "id": 40,
                      "name": "Alex",
                      "lastName": "Turner",
                      "email": "alexturner@gmail.com",
                      "document": "94387634945",
                      "phoneNumber": "54999998888",
                      "createdAt": "2024-05-20T14:30:00",
                      "updatedAt": "2024-05-20T14:30:00"
                }
                """;

        assertThat(json.parse(expected)).isEqualTo(
                new Consumer(
                        40L,
                        "Alex",
                        "Turner",
                        "alexturner@gmail.com",
                        "94387634945",
                        "54999998888",
                        LocalDateTime.parse("2024-05-20T14:30:00"),
                        LocalDateTime.parse("2024-05-20T14:30:00")
                ));

        assertThat(json.parseObject(expected).id()).isEqualTo(40);
        assertThat(json.parseObject(expected).name()).isEqualTo("Alex");
        assertThat(json.parseObject(expected).lastName()).isEqualTo("Turner");
        assertThat(json.parseObject(expected).email()).isEqualTo("alexturner@gmail.com");
        assertThat(json.parseObject(expected).document()).isEqualTo("94387634945");
        assertThat(json.parseObject(expected).phoneNumber()).isEqualTo("54999998888");
        assertThat(json.parseObject(expected).createdAt()).isEqualTo(LocalDateTime.parse("2024-05-20T14:30:00"));
        assertThat(json.parseObject(expected).updatedAt()).isEqualTo(LocalDateTime.parse("2024-05-20T14:30:00"));
    }
}
