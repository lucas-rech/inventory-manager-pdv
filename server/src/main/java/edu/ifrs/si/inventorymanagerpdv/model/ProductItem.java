package edu.ifrs.si.inventorymanagerpdv.model;

import java.time.LocalDateTime;

import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Table;

@Table(name = "product_item")
public record ProductItem(
        @Id Long id,
        String name,
        String description,
        String gtin,
        String ncm,
        Double price,
        Double cost,
        LocalDateTime createdAt,
        LocalDateTime updatedAt) {
}
