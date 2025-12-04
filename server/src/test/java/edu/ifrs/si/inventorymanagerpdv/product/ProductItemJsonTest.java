package edu.ifrs.si.inventorymanagerpdv.product;

import edu.ifrs.si.inventorymanagerpdv.model.ProductItem;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.json.JsonTest;
import org.springframework.boot.test.json.JacksonTester;

import java.io.IOException;
import java.time.LocalDateTime;

import static org.assertj.core.api.Assertions.assertThat;

@JsonTest
public class ProductItemJsonTest {

    @Autowired
    private JacksonTester<ProductItem> json;

    @Autowired
    private JacksonTester<ProductItem[]> jsonList;

    private ProductItem[] productItems;

    @BeforeEach
    void setUp() {
        productItems = new ProductItem[] {
            new ProductItem(1L, "Fandangos", "Salgadinho sabor queijo", "7891991000137", "19059020", 9.50, 5.00, LocalDateTime.parse("2023-01-10T10:00:00"), LocalDateTime.parse("2023-01-10T12:00:00")),
            new ProductItem(2L, "Coca-Cola Lata 350ml", "Refrigerante tradicional", "7894900011517", "22021000", 5.00, 2.80, LocalDateTime.parse("2023-01-10T10:05:00"), LocalDateTime.parse("2023-01-10T12:05:00")),
            new ProductItem(3L, "Doritos Queijo Nacho", "Salgadinho de milho sabor queijo nacho", "7892840810163", "19059020", 11.00, 6.50, LocalDateTime.parse("2023-01-10T10:10:00"), LocalDateTime.parse("2023-01-10T12:10:00")),
            new ProductItem(4L, "Guaraná Antarctica 2L", "Refrigerante de guaraná", "7891991000834", "22021000", 9.80, 5.00, LocalDateTime.parse("2023-01-10T10:15:00"), LocalDateTime.parse("2023-01-10T12:15:00")),
            new ProductItem(5L, "Ruffles Original", "Batata frita ondulada sabor original", "7892840810101", "19059020", 10.50, 6.00, LocalDateTime.parse("2023-01-10T10:20:00"), LocalDateTime.parse("2023-01-10T12:20:00")),
            new ProductItem(6L, "Trakinas Chocolate", "Biscoito recheado sabor chocolate", "7892840220474", "19053100", 4.50, 2.00, LocalDateTime.parse("2023-01-10T10:25:00"), LocalDateTime.parse("2023-01-10T12:25:00")),
            new ProductItem(7L, "Club Social Original", "Biscoito salgado tradicional", "7894900700459", "19053100", 3.20, 1.50, LocalDateTime.parse("2023-01-10T10:30:00"), LocalDateTime.parse("2023-01-10T12:30:00")),
            new ProductItem(8L, "Oreo Baunilha", "Biscoito recheado com creme de baunilha", "7892840220566", "19053100", 5.20, 2.30, LocalDateTime.parse("2023-01-10T10:35:00"), LocalDateTime.parse("2023-01-10T12:35:00")),
            new ProductItem(9L, "Nescau 2.0 400g", "Achocolatado em pó", "7891000066786", "18069000", 9.00, 5.00, LocalDateTime.parse("2023-01-10T10:40:00"), LocalDateTime.parse("2023-01-10T12:40:00")),
            new ProductItem(10L, "Leite Integral Italac 1L", "Leite UHT integral", "7898215150159", "04012010", 4.90, 3.20, LocalDateTime.parse("2023-01-10T10:45:00"), LocalDateTime.parse("2023-01-10T12:45:00")),
            new ProductItem(11L, "Arroz Tio João 5kg", "Arroz branco tipo 1", "7896040700020", "10063021", 28.90, 19.00, LocalDateTime.parse("2023-01-10T10:50:00"), LocalDateTime.parse("2023-01-10T12:50:00")),
            new ProductItem(12L, "Feijão Carioca Camil 1kg", "Feijão carioca tipo 1", "7896006740010", "07133329", 8.50, 5.50, LocalDateTime.parse("2023-01-10T10:55:00"), LocalDateTime.parse("2023-01-10T12:55:00")),
            new ProductItem(13L, "Macarrão Renata Espaguete", "Massa de trigo tipo espaguete", "7896276700322", "19021900", 6.20, 3.50, LocalDateTime.parse("2023-01-10T11:00:00"), LocalDateTime.parse("2023-01-10T13:00:00")),
            new ProductItem(14L, "Molho de Tomate Heinz", "Molho tradicional em sachê", "7891991002326", "21032010", 4.80, 2.50, LocalDateTime.parse("2023-01-10T11:05:00"), LocalDateTime.parse("2023-01-10T13:05:00")),
            new ProductItem(15L, "Açúcar União 1kg", "Açúcar refinado branco", "7891910000197", "17019900", 4.10, 2.80, LocalDateTime.parse("2023-01-10T11:10:00"), LocalDateTime.parse("2023-01-10T13:10:00")),
            new ProductItem(16L, "Sal Cisne 1kg", "Sal refinado iodado", "7896036090108", "25010012", 2.30, 1.20, LocalDateTime.parse("2023-01-10T11:15:00"), LocalDateTime.parse("2023-01-10T13:15:00")),
            new ProductItem(17L, "Café Pilão 500g", "Café torrado e moído", "7896005800012", "09012100", 14.90, 9.80, LocalDateTime.parse("2023-01-10T11:20:00"), LocalDateTime.parse("2023-01-10T13:20:00")),
            new ProductItem(18L, "Miojo Galinha Caipira", "Macarrão instantâneo sabor galinha caipira", "7891079000013", "19023000", 2.20, 1.00, LocalDateTime.parse("2023-01-10T11:25:00"), LocalDateTime.parse("2023-01-10T13:25:00")),
            new ProductItem(19L, "Leite Condensado Moça", "Leite condensado tradicional 395g", "7891000060500", "04029910", 7.80, 4.50, LocalDateTime.parse("2023-01-10T11:30:00"), LocalDateTime.parse("2023-01-10T13:30:00")),
            new ProductItem(20L, "Creme de Leite Nestlé", "Creme de leite em lata 300g", "7891000070004", "04015000", 5.90, 3.20, LocalDateTime.parse("2023-01-10T11:35:00"), LocalDateTime.parse("2023-01-10T13:35:00")),
            new ProductItem(21L, "Sabonete Dove", "Sabonete hidratante 90g", "7891150005312", "34011190", 4.50, 2.30, LocalDateTime.parse("2023-01-10T11:40:00"), LocalDateTime.parse("2023-01-10T13:40:00")),
            new ProductItem(22L, "Shampoo Seda Liso Perfeito", "Shampoo 325ml", "7891150021152", "33051000", 11.90, 6.00, LocalDateTime.parse("2023-01-10T11:45:00"), LocalDateTime.parse("2023-01-10T13:45:00")),
            new ProductItem(23L, "Condicionador Seda Liso Perfeito", "Condicionador 325ml", "7891150021169", "33052000", 12.50, 6.30, LocalDateTime.parse("2023-01-10T11:50:00"), LocalDateTime.parse("2023-01-10T13:50:00")),
            new ProductItem(24L, "Sabão em Pó OMO 1kg", "Sabão em pó para roupas", "7891150022500", "34022000", 12.90, 8.00, LocalDateTime.parse("2023-01-10T11:55:00"), LocalDateTime.parse("2023-01-10T13:55:00")),
            new ProductItem(25L, "Detergente Ypê Neutro 500ml", "Detergente líquido neutro", "7896094900060", "34022000", 2.50, 1.20, LocalDateTime.parse("2023-01-10T12:00:00"), LocalDateTime.parse("2023-01-10T14:00:00")),
            new ProductItem(26L, "Desinfetante Pinho Sol 500ml", "Desinfetante multiuso", "7891150000539", "38089411", 8.90, 4.60, LocalDateTime.parse("2023-01-10T12:05:00"), LocalDateTime.parse("2023-01-10T14:05:00")),
            new ProductItem(27L, "Papel Higiênico Neve 12x30m", "Papel higiênico folha dupla", "7891150000904", "48181000", 25.90, 17.00, LocalDateTime.parse("2023-01-10T12:10:00"), LocalDateTime.parse("2023-01-10T14:10:00")),
            new ProductItem(28L, "Escova de Dentes Colgate", "Escova dental média", "7891150049026", "96032100", 7.50, 3.90, LocalDateTime.parse("2023-01-10T12:15:00"), LocalDateTime.parse("2023-01-10T14:15:00")),
            new ProductItem(29L, "Pasta de Dente Colgate Total 90g", "Creme dental proteção completa", "7891150049019", "33061000", 9.50, 4.80, LocalDateTime.parse("2023-01-10T12:20:00"), LocalDateTime.parse("2023-01-10T14:20:00")),
            new ProductItem(30L, "Desodorante Rexona Aerosol", "Desodorante antitranspirante 150ml", "7891150032400", "33072010", 14.90, 8.90, LocalDateTime.parse("2023-01-10T12:25:00"), LocalDateTime.parse("2023-01-10T14:25:00"))
        };
    }

    @Test
    void productItemSerializationTest() throws IOException {
        ProductItem productItem = new ProductItem(
                1L,
                "Fandangos",
                "Salgadinho sabor queijo",
                "7891991000137",
                "19059020",
                9.5,
                5.0,
                LocalDateTime.parse("2023-10-01T10:00:00"),
                LocalDateTime.parse("2023-10-15T12:00:00")
        );

        assertThat(json.write(productItem)).isStrictlyEqualToJson("single-product.json");
        assertThat(json.write(productItem)).hasJsonPathNumberValue("@.id");
        assertThat(json.write(productItem)).hasJsonPathStringValue("@.name");
        assertThat(json.write(productItem)).hasJsonPathStringValue("@.description");
        assertThat(json.write(productItem)).hasJsonPathStringValue("@.gtin");
        assertThat(json.write(productItem)).hasJsonPathStringValue("@.ncm");
        assertThat(json.write(productItem)).hasJsonPathNumberValue("@.price");
        assertThat(json.write(productItem)).hasJsonPathNumberValue("@.cost");
        assertThat(json.write(productItem)).hasJsonPathStringValue("@.createdAt");
        assertThat(json.write(productItem)).hasJsonPathStringValue("@.updatedAt");

        assertThat(json.write(productItem)).extractingJsonPathNumberValue("@.id").isEqualTo(1);
        assertThat(json.write(productItem)).extractingJsonPathStringValue("@.name").isEqualTo("Fandangos");
        assertThat(json.write(productItem)).extractingJsonPathStringValue("@.description").isEqualTo("Salgadinho sabor queijo");
        assertThat(json.write(productItem)).extractingJsonPathStringValue("@.gtin").isEqualTo("7891991000137");
        assertThat(json.write(productItem)).extractingJsonPathStringValue("@.ncm").isEqualTo("19059020");
        assertThat(json.write(productItem)).extractingJsonPathNumberValue("@.price").isEqualTo(9.5);
        assertThat(json.write(productItem)).extractingJsonPathNumberValue("@.cost").isEqualTo(5.0);
        assertThat(json.write(productItem)).extractingJsonPathStringValue("@.createdAt").isEqualTo("2023-10-01T10:00:00");
        assertThat(json.write(productItem)).extractingJsonPathStringValue("@.updatedAt").isEqualTo("2023-10-15T12:00:00");
    }

    @Test
    void ProductItemDeserializationTest() throws IOException {
        String expected = """
                {
                    "id": 1,
                    "name": "Fandangos",
                    "description": "Salgadinho sabor queijo",
                    "gtin": "7891991000137",
                    "ncm": "19059020",
                    "price": 9.5,
                    "cost": 5.0,
                    "createdAt": "2023-10-01T10:00:00",
                    "updatedAt": "2023-10-15T12:00:00"
                }
                """;
        
        assertThat(json.parse(expected))
                .isEqualTo(new ProductItem(
                    1L,
                    "Fandangos",
                    "Salgadinho sabor queijo", 
                    "7891991000137", 
                    "19059020", 
                    9.5, 
                    5.0, 
                    LocalDateTime.parse("2023-10-01T10:00:00"), 
                    LocalDateTime.parse("2023-10-15T12:00:00")
                ));
        assertThat(json.parseObject(expected).id()).isEqualTo(1L);
        assertThat(json.parseObject(expected).name()).isEqualTo("Fandangos");
        assertThat(json.parseObject(expected).description()).isEqualTo("Salgadinho sabor queijo");
        assertThat(json.parseObject(expected).gtin()).isEqualTo("7891991000137");
        assertThat(json.parseObject(expected).ncm()).isEqualTo("19059020");
        assertThat(json.parseObject(expected).price()).isEqualTo(9.5);
        assertThat(json.parseObject(expected).cost()).isEqualTo(5.0);
        assertThat(json.parseObject(expected).createdAt()).isEqualTo("2023-10-01T10:00:00");
        assertThat(json.parseObject(expected).updatedAt()).isEqualTo("2023-10-15T12:00:00");
    }


    @Test
    void productItemListSerializationTest()  throws IOException {
        assertThat(jsonList.write(productItems)).isStrictlyEqualToJson("list-product.json");
    }

    
    @Test
    void productItemListDeserializationTest() throws IOException {
        String expected = """
                    [
                        {
                            "id": 1,
                            "name": "Fandangos",
                            "description": "Salgadinho sabor queijo",
                            "gtin": "7891991000137",
                            "ncm": "19059020",
                            "price": 9.50,
                            "cost": 5.00,
                            "createdAt": "2023-01-10T10:00:00",
                            "updatedAt": "2023-01-10T12:00:00"
                        },
                        {
                            "id": 2,
                            "name": "Coca-Cola Lata 350ml",
                            "description": "Refrigerante tradicional",
                            "gtin": "7894900011517",
                            "ncm": "22021000",
                            "price": 5.00,
                            "cost": 2.80,
                            "createdAt": "2023-01-10T10:05:00",
                            "updatedAt": "2023-01-10T12:05:00"
                        },
                        {
                            "id": 3,
                            "name": "Doritos Queijo Nacho",
                            "description": "Salgadinho de milho sabor queijo nacho",
                            "gtin": "7892840810163",
                            "ncm": "19059020",
                            "price": 11.00,
                            "cost": 6.50,
                            "createdAt": "2023-01-10T10:10:00",
                            "updatedAt": "2023-01-10T12:10:00"
                        },
                        {
                            "id": 4,
                            "name": "Guaraná Antarctica 2L",
                            "description": "Refrigerante de guaraná",
                            "gtin": "7891991000834",
                            "ncm": "22021000",
                            "price": 9.80,
                            "cost": 5.00,
                            "createdAt": "2023-01-10T10:15:00",
                            "updatedAt": "2023-01-10T12:15:00"
                        },
                        {
                            "id": 5,
                            "name": "Ruffles Original",
                            "description": "Batata frita ondulada sabor original",
                            "gtin": "7892840810101",
                            "ncm": "19059020",
                            "price": 10.50,
                            "cost": 6.00,
                            "createdAt": "2023-01-10T10:20:00",
                            "updatedAt": "2023-01-10T12:20:00"
                        },
                        {
                            "id": 6,
                            "name": "Trakinas Chocolate",
                            "description": "Biscoito recheado sabor chocolate",
                            "gtin": "7892840220474",
                            "ncm": "19053100",
                            "price": 4.50,
                            "cost": 2.00,
                            "createdAt": "2023-01-10T10:25:00",
                            "updatedAt": "2023-01-10T12:25:00"
                        },
                        {
                            "id": 7,
                            "name": "Club Social Original",
                            "description": "Biscoito salgado tradicional",
                            "gtin": "7894900700459",
                            "ncm": "19053100",
                            "price": 3.20,
                            "cost": 1.50,
                            "createdAt": "2023-01-10T10:30:00",
                            "updatedAt": "2023-01-10T12:30:00"
                        },
                        {
                            "id": 8,
                            "name": "Oreo Baunilha",
                            "description": "Biscoito recheado com creme de baunilha",
                            "gtin": "7892840220566",
                            "ncm": "19053100",
                            "price": 5.20,
                            "cost": 2.30,
                            "createdAt": "2023-01-10T10:35:00",
                            "updatedAt": "2023-01-10T12:35:00"
                        },
                        {
                            "id": 9,
                            "name": "Nescau 2.0 400g",
                            "description": "Achocolatado em pó",
                            "gtin": "7891000066786",
                            "ncm": "18069000",
                            "price": 9.00,
                            "cost": 5.00,
                            "createdAt": "2023-01-10T10:40:00",
                            "updatedAt": "2023-01-10T12:40:00"
                        },
                        {
                            "id": 10,
                            "name": "Leite Integral Italac 1L",
                            "description": "Leite UHT integral",
                            "gtin": "7898215150159",
                            "ncm": "04012010",
                            "price": 4.90,
                            "cost": 3.20,
                            "createdAt": "2023-01-10T10:45:00",
                            "updatedAt": "2023-01-10T12:45:00"
                        },
                        {
                            "id": 11,
                            "name": "Arroz Tio João 5kg",
                            "description": "Arroz branco tipo 1",
                            "gtin": "7896040700020",
                            "ncm": "10063021",
                            "price": 28.90,
                            "cost": 19.00,
                            "createdAt": "2023-01-10T10:50:00",
                            "updatedAt": "2023-01-10T12:50:00"
                        },
                        {
                            "id": 12,
                            "name": "Feijão Carioca Camil 1kg",
                            "description": "Feijão carioca tipo 1",
                            "gtin": "7896006740010",
                            "ncm": "07133329",
                            "price": 8.50,
                            "cost": 5.50,
                            "createdAt": "2023-01-10T10:55:00",
                            "updatedAt": "2023-01-10T12:55:00"
                        },
                        {
                            "id": 13,
                            "name": "Macarrão Renata Espaguete",
                            "description": "Massa de trigo tipo espaguete",
                            "gtin": "7896276700322",
                            "ncm": "19021900",
                            "price": 6.20,
                            "cost": 3.50,
                            "createdAt": "2023-01-10T11:00:00",
                            "updatedAt": "2023-01-10T13:00:00"
                        },
                        {
                            "id": 14,
                            "name": "Molho de Tomate Heinz",
                            "description": "Molho tradicional em sachê",
                            "gtin": "7891991002326",
                            "ncm": "21032010",
                            "price": 4.80,
                            "cost": 2.50,
                            "createdAt": "2023-01-10T11:05:00",
                            "updatedAt": "2023-01-10T13:05:00"
                        },
                        {
                            "id": 15,
                            "name": "Açúcar União 1kg",
                            "description": "Açúcar refinado branco",
                            "gtin": "7891910000197",
                            "ncm": "17019900",
                            "price": 4.10,
                            "cost": 2.80,
                            "createdAt": "2023-01-10T11:10:00",
                            "updatedAt": "2023-01-10T13:10:00"
                        },
                        {
                            "id": 16,
                            "name": "Sal Cisne 1kg",
                            "description": "Sal refinado iodado",
                            "gtin": "7896036090108",
                            "ncm": "25010012",
                            "price": 2.30,
                            "cost": 1.20,
                            "createdAt": "2023-01-10T11:15:00",
                            "updatedAt": "2023-01-10T13:15:00"
                        },
                        {
                            "id": 17,
                            "name": "Café Pilão 500g",
                            "description": "Café torrado e moído",
                            "gtin": "7896005800012",
                            "ncm": "09012100",
                            "price": 14.90,
                            "cost": 9.80,
                            "createdAt": "2023-01-10T11:20:00",
                            "updatedAt": "2023-01-10T13:20:00"
                        },
                        {
                            "id": 18,
                            "name": "Miojo Galinha Caipira",
                            "description": "Macarrão instantâneo sabor galinha caipira",
                            "gtin": "7891079000013",
                            "ncm": "19023000",
                            "price": 2.20,
                            "cost": 1.00,
                            "createdAt": "2023-01-10T11:25:00",
                            "updatedAt": "2023-01-10T13:25:00"
                        },
                        {
                            "id": 19,
                            "name": "Leite Condensado Moça",
                            "description": "Leite condensado tradicional 395g",
                            "gtin": "7891000060500",
                            "ncm": "04029910",
                            "price": 7.80,
                            "cost": 4.50,
                            "createdAt": "2023-01-10T11:30:00",
                            "updatedAt": "2023-01-10T13:30:00"
                        },
                        {
                            "id": 20,
                            "name": "Creme de Leite Nestlé",
                            "description": "Creme de leite em lata 300g",
                            "gtin": "7891000070004",
                            "ncm": "04015000",
                            "price": 5.90,
                            "cost": 3.20,
                            "createdAt": "2023-01-10T11:35:00",
                            "updatedAt": "2023-01-10T13:35:00"
                        },
                        {
                            "id": 21,
                            "name": "Sabonete Dove",
                            "description": "Sabonete hidratante 90g",
                            "gtin": "7891150005312",
                            "ncm": "34011190",
                            "price": 4.50,
                            "cost": 2.30,
                            "createdAt": "2023-01-10T11:40:00",
                            "updatedAt": "2023-01-10T13:40:00"
                        },
                        {
                            "id": 22,
                            "name": "Shampoo Seda Liso Perfeito",
                            "description": "Shampoo 325ml",
                            "gtin": "7891150021152",
                            "ncm": "33051000",
                            "price": 11.90,
                            "cost": 6.00,
                            "createdAt": "2023-01-10T11:45:00",
                            "updatedAt": "2023-01-10T13:45:00"
                        },
                        {
                            "id": 23,
                            "name": "Condicionador Seda Liso Perfeito",
                            "description": "Condicionador 325ml",
                            "gtin": "7891150021169",
                            "ncm": "33052000",
                            "price": 12.50,
                            "cost": 6.30,
                            "createdAt": "2023-01-10T11:50:00",
                            "updatedAt": "2023-01-10T13:50:00"
                        },
                        {
                            "id": 24,
                            "name": "Sabão em Pó OMO 1kg",
                            "description": "Sabão em pó para roupas",
                            "gtin": "7891150022500",
                            "ncm": "34022000",
                            "price": 12.90,
                            "cost": 8.00,
                            "createdAt": "2023-01-10T11:55:00",
                            "updatedAt": "2023-01-10T13:55:00"
                        },
                        {
                            "id": 25,
                            "name": "Detergente Ypê Neutro 500ml",
                            "description": "Detergente líquido neutro",
                            "gtin": "7896094900060",
                            "ncm": "34022000",
                            "price": 2.50,
                            "cost": 1.20,
                            "createdAt": "2023-01-10T12:00:00",
                            "updatedAt": "2023-01-10T14:00:00"
                        },
                        {
                            "id": 26,
                            "name": "Desinfetante Pinho Sol 500ml",
                            "description": "Desinfetante multiuso",
                            "gtin": "7891150000539",
                            "ncm": "38089411",
                            "price": 8.90,
                            "cost": 4.60,
                            "createdAt": "2023-01-10T12:05:00",
                            "updatedAt": "2023-01-10T14:05:00"
                        },
                        {
                            "id": 27,
                            "name": "Papel Higiênico Neve 12x30m",
                            "description": "Papel higiênico folha dupla",
                            "gtin": "7891150000904",
                            "ncm": "48181000",
                            "price": 25.90,
                            "cost": 17.00,
                            "createdAt": "2023-01-10T12:10:00",
                            "updatedAt": "2023-01-10T14:10:00"
                        },
                        {
                            "id": 28,
                            "name": "Escova de Dentes Colgate",
                            "description": "Escova dental média",
                            "gtin": "7891150049026",
                            "ncm": "96032100",
                            "price": 7.50,
                            "cost": 3.90,
                            "createdAt": "2023-01-10T12:15:00",
                            "updatedAt": "2023-01-10T14:15:00"
                        },
                        {
                            "id": 29,
                            "name": "Pasta de Dente Colgate Total 90g",
                            "description": "Creme dental proteção completa",
                            "gtin": "7891150049019",
                            "ncm": "33061000",
                            "price": 9.50,
                            "cost": 4.80,
                            "createdAt": "2023-01-10T12:20:00",
                            "updatedAt": "2023-01-10T14:20:00"
                        },
                        {
                            "id": 30,
                            "name": "Desodorante Rexona Aerosol",
                            "description": "Desodorante antitranspirante 150ml",
                            "gtin": "7891150032400",
                            "ncm": "33072010",
                            "price": 14.90,
                            "cost": 8.90,
                            "createdAt": "2023-01-10T12:25:00",
                            "updatedAt": "2023-01-10T14:25:00"
                        }
                    ]
                """;
        assertThat(jsonList.parse(expected)).isEqualTo(productItems);
    }
}
