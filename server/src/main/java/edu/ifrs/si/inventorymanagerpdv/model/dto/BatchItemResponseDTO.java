package edu.ifrs.si.inventorymanagerpdv.model.dto;

import edu.ifrs.si.inventorymanagerpdv.model.Batch;

import java.time.LocalDateTime;

public record BatchItemResponseDTO(
        Long id,
        String batchId,
        ProductBatchDTO product,
        Double cost,
        Integer quantity,
        LocalDateTime validationDate,
        LocalDateTime createdAt,
        LocalDateTime updatedAt
) {
}
