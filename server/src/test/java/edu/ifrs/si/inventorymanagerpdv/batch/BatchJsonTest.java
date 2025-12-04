package edu.ifrs.si.inventorymanagerpdv.batch;

import static org.assertj.core.api.Assertions.assertThat;

import java.io.IOException;
import java.time.LocalDateTime;

import edu.ifrs.si.inventorymanagerpdv.model.dto.BatchItemResponseDTO;
import edu.ifrs.si.inventorymanagerpdv.model.dto.ProductBatchDTO;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.json.JsonTest;
import org.springframework.boot.test.json.JacksonTester;



@JsonTest
public class BatchJsonTest {

    @Autowired
    private JacksonTester<BatchItemResponseDTO> json;
    private ProductBatchDTO productBatchDTO;

    @BeforeEach
    void setUp() {
        this.productBatchDTO = new ProductBatchDTO(1L, "Fandangos");
    }

    @Test
    void batchSerializationTest() throws IOException {
        BatchItemResponseDTO batch = new BatchItemResponseDTO(
            1L, 
            "123ABC456",
            productBatchDTO,
            200.00,
            350, 
            LocalDateTime.parse("2023-10-01T10:00:00"), 
            LocalDateTime.parse("2023-10-01T10:00:00"), 
            LocalDateTime.parse("2023-10-01T10:00:00")
        );

        assertThat(json.write(batch)).isStrictlyEqualToJson("single-batch.json");
        assertThat(json.write(batch)).extractingJsonPathNumberValue("@.id").isEqualTo(1);
        assertThat(json.write(batch)).extractingJsonPathStringValue("@.batchId").isEqualTo("123ABC456");
        assertThat(json.write(batch)).extractingJsonPathNumberValue("@.product.id").isEqualTo(1);
        assertThat(json.write(batch)).extractingJsonPathStringValue("@.product.name").isEqualTo("Fandangos");
        assertThat(json.write(batch)).extractingJsonPathNumberValue("@.cost").isEqualTo(200.00);
        assertThat(json.write(batch)).extractingJsonPathStringValue("@.validationDate").isEqualTo("2023-10-01T10:00:00");
        assertThat(json.write(batch)).extractingJsonPathStringValue("@.createdAt").isEqualTo("2023-10-01T10:00:00");
        assertThat(json.write(batch)).extractingJsonPathStringValue("@.updatedAt").isEqualTo("2023-10-01T10:00:00");
    }

    @Test
    void batchDeserializationTest() throws IOException {
        String expected = """
                {
                    "id": 1,
                    "batchId": "123ABC456",
                    "product": {
                        "id": 1,
                        "name": "Fandangos"
                    },
                    "cost": 200.00,
                    "quantity": 350,
                    "validationDate": "2023-10-01T10:00:00",
                    "createdAt": "2023-10-01T10:00:00",
                    "updatedAt": "2023-10-01T10:00:00"
                }
                """;
        
        assertThat(json.parse(expected)).isEqualTo(
            new BatchItemResponseDTO(
                1L, 
                "123ABC456", 
                productBatchDTO,
                200.00, 
                350, 
                LocalDateTime.parse("2023-10-01T10:00:00"), 
                LocalDateTime.parse("2023-10-01T10:00:00"),
                LocalDateTime.parse("2023-10-01T10:00:00"))
        );

        assertThat(json.parseObject(expected).id()).isEqualTo(1);
        assertThat(json.parseObject(expected).batchId()).isEqualTo("123ABC456");
        assertThat(json.parseObject(expected).product().id()).isEqualTo(1);
        assertThat(json.parseObject(expected).product().name()).isEqualTo("Fandangos");
        assertThat(json.parseObject(expected).cost()).isEqualTo(200.00);
        assertThat(json.parseObject(expected).quantity()).isEqualTo(350);
        assertThat(json.parseObject(expected).validationDate()).isEqualTo("2023-10-01T10:00:00");
        assertThat(json.parseObject(expected).createdAt()).isEqualTo("2023-10-01T10:00:00");
        assertThat(json.parseObject(expected).updatedAt()).isEqualTo("2023-10-01T10:00:00");
    }


}
