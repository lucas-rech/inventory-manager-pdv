package edu.ifrs.si.inventorymanagerpdv.user;

import edu.ifrs.si.inventorymanagerpdv.model.Role;
import edu.ifrs.si.inventorymanagerpdv.model.User;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.json.JsonTest;
import org.springframework.boot.test.json.JacksonTester;

import java.io.IOException;
import java.time.LocalDateTime;

import static org.assertj.core.api.Assertions.assertThat;

@JsonTest
public class UserJsonTest {

    @Autowired
    private JacksonTester<User> json;

    @Test
    void userSerializationTest() throws IOException {
        User user = new User(
                1L,
                "Lucas Rech",
                "lucasrech00",
                "54996041744",
                Role.ADMIN,
                "abc123",
                LocalDateTime.parse("2023-10-01T10:00:00"),
                LocalDateTime.parse("2023-10-01T10:00:00"),
                false
        );

        assertThat(json.write(user)).isStrictlyEqualToJson("single-user.json");
        assertThat(json.write(user)).hasJsonPathNumberValue("$.id");
        assertThat(json.write(user)).extractingJsonPathNumberValue("id").isEqualTo(1);
        assertThat(json.write(user)).hasJsonPathStringValue("$.name");
        assertThat(json.write(user)).extractingJsonPathStringValue("name").isEqualTo("Lucas Rech");
        assertThat(json.write(user)).hasJsonPathStringValue("$.username");
        assertThat(json.write(user)).extractingJsonPathStringValue("username").isEqualTo("lucasrech00");
        assertThat(json.write(user)).hasJsonPathStringValue("$.phoneNumber");
        assertThat(json.write(user)).extractingJsonPathStringValue("$.phoneNumber").isEqualTo("54996041744");
        assertThat(json.write(user)).hasJsonPathStringValue("$.role");
        assertThat(json.write(user)).extractingJsonPathStringValue("role").isEqualTo("ADMIN");
        assertThat(json.write(user)).hasJsonPathStringValue("$.password");
        assertThat(json.write(user)).extractingJsonPathStringValue("password").isEqualTo("abc123");
        assertThat(json.write(user)).hasJsonPathStringValue("$.createdAt");
        assertThat(json.write(user)).extractingJsonPathStringValue("createdAt").isEqualTo("2023-10-01T10:00:00");
        assertThat(json.write(user)).hasJsonPathStringValue("$.updatedAt");
        assertThat(json.write(user)).extractingJsonPathStringValue("updatedAt").isEqualTo("2023-10-01T10:00:00");
        assertThat(json.write(user)).hasJsonPathBooleanValue("$.deleted");
        assertThat(json.write(user)).extractingJsonPathBooleanValue("deleted").isEqualTo(false);
    }

    @Test
    void userDeserializationTest() throws IOException {
        String expected = """
                    {
                      "id": 1,
                      "name": "Lucas Rech",
                      "username": "lucasrech00",
                      "phoneNumber": "54996041744",
                      "role": "ADMIN",
                      "password": "abc123",
                      "createdAt": "2023-10-01T10:00:00",
                      "updatedAt": "2023-10-01T10:00:00",
                      "deleted": false
                    }
                """;

        assertThat(json.parse(expected)).isEqualTo(
                new User(
                        1L,
                        "Lucas Rech",
                        "lucasrech00",
                        "54996041744",
                        Role.ADMIN,
                        "abc123",
                        LocalDateTime.parse("2023-10-01T10:00:00"),
                        LocalDateTime.parse("2023-10-01T10:00:00"),
                        false
                )
        );

        assertThat(json.parseObject(expected).id()).isEqualTo(1);
        assertThat(json.parseObject(expected).name()).isEqualTo("Lucas Rech");
        assertThat(json.parseObject(expected).username()).isEqualTo("lucasrech00");
        assertThat(json.parseObject(expected).phoneNumber()).isEqualTo("54996041744");
        assertThat(json.parseObject(expected).role()).isEqualTo(Role.ADMIN);
        assertThat(json.parseObject(expected).password()).isEqualTo("abc123");
        assertThat(json.parseObject(expected).createdAt()).isEqualTo("2023-10-01T10:00:00");
        assertThat(json.parseObject(expected).updatedAt()).isEqualTo("2023-10-01T10:00:00");
        assertThat(json.parseObject(expected).deleted()).isEqualTo(false);
    }
}
