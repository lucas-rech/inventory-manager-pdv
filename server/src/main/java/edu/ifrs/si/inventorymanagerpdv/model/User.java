package edu.ifrs.si.inventorymanagerpdv.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Table;

import java.time.LocalDateTime;

@Table(name = "app_user")
public record User(
        @Id Long id,
        String name,
        String username,
        String phoneNumber,
        Role role,
        String password,
        LocalDateTime createdAt,
        LocalDateTime updatedAt,
        boolean deleted
) {
}
