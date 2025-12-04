package edu.ifrs.si.inventorymanagerpdv.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Table;

import java.time.LocalDateTime;

@Table(name = "consumer")
public record Consumer(
        @Id Long id,
        String name,
        String lastName,
        String email,
        String document,
        String phoneNumber,
        LocalDateTime createdAt,
        LocalDateTime updatedAt
) {
}
