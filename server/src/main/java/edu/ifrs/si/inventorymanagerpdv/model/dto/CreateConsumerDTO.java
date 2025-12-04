package edu.ifrs.si.inventorymanagerpdv.model.dto;

public record CreateConsumerDTO(
        String name,
        String lastName,
        String email,
        String document,
        String phoneNumber
) {
}
