package edu.ifrs.si.inventorymanagerpdv.controller;

import java.net.URI;
import java.util.List;

import edu.ifrs.si.inventorymanagerpdv.model.ProductItem;
import edu.ifrs.si.inventorymanagerpdv.model.dto.BatchItemResponseDTO;
import edu.ifrs.si.inventorymanagerpdv.model.dto.ProductBatchDTO;
import edu.ifrs.si.inventorymanagerpdv.service.ProductItemService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import edu.ifrs.si.inventorymanagerpdv.model.Batch;
import edu.ifrs.si.inventorymanagerpdv.service.BatchService;
import org.springframework.web.util.UriComponentsBuilder;

@RestController
@RequestMapping("/batches")
public class BatchController {

    private final BatchService batchService;
    private final ProductItemService productItemService;

    public BatchController(BatchService batchService, ProductItemService productItemService) {
        this.batchService = batchService;
        this.productItemService = productItemService;
    }

    @GetMapping("/{id}")
    public ResponseEntity<BatchItemResponseDTO> findBatchById(@PathVariable Long id) {
        Batch batch = batchService.findById(id);
        if (batch == null) {
            return ResponseEntity.notFound().build();
        }

        ProductItem productItem = productItemService.getProductItemById(batch.productId());
        BatchItemResponseDTO response = new BatchItemResponseDTO(
                batch.id(),
                batch.batchId(),
                new ProductBatchDTO(productItem.id(), productItem.name()),
                batch.cost(),
                batch.quantity(),
                batch.validationDate(),
                batch.createdAt(),
                batch.updatedAt()
        );
        return ResponseEntity.ok(response);
    }


    @GetMapping()
    public ResponseEntity<List<BatchItemResponseDTO>> getBatchesForProductId(@RequestParam(required = true) Long product){
        List<Batch> batches = batchService.findBatchesByProductId(product);
        if (batches.isEmpty()) {
            return ResponseEntity.notFound().build();
        }

        ProductItem productItem = productItemService.getProductItemById(product);
        if (productItem == null) {
            return ResponseEntity.notFound().build();
        }

        List<BatchItemResponseDTO> response = batches.stream()
                .map(batch -> new BatchItemResponseDTO(
                    batch.id(),
                    batch.batchId(),
                    new ProductBatchDTO(productItem.id(), productItem.name()),
                    batch.cost(),
                    batch.quantity(),
                    batch.validationDate(),
                    batch.createdAt(),
                    batch.updatedAt()
                ))
                .toList();

        return ResponseEntity.ok(response);
    }

    @PostMapping
    public ResponseEntity<Void> createBatch(@RequestBody Batch batch, UriComponentsBuilder ucb){
        Batch request = batchService.createBatch(batch);
        if (request == null) return ResponseEntity.badRequest().build();

        URI locationOfNewBatch = ucb
                .path("/batches/{id}")
                .buildAndExpand(request.id())
                .toUri();
        return ResponseEntity.created(locationOfNewBatch).build();
    }


    @PatchMapping("consume/{productId}")
    public ResponseEntity<Integer> consumeInventoryByProductId(
            @PathVariable Long productId,
            @RequestParam Integer quantity
    ) {
        Integer consumedQuantity = batchService.consumeInventoryByProductId(productId, quantity);
        return ResponseEntity.ok(consumedQuantity);
    }
}
