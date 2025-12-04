package edu.ifrs.si.inventorymanagerpdv.service;

import java.security.InvalidParameterException;
import java.time.LocalDateTime;
import java.util.List;

import edu.ifrs.si.inventorymanagerpdv.config.exceptions.BatchNotFoundExcption;
import org.springframework.stereotype.Service;

import edu.ifrs.si.inventorymanagerpdv.model.Batch;
import edu.ifrs.si.inventorymanagerpdv.model.ProductItem;
import edu.ifrs.si.inventorymanagerpdv.repository.BatchRepository;

@Service
public class BatchService {

    private final BatchRepository batchRepository;
    private final ProductItemService productItemService;

    public BatchService(BatchRepository batchRepository, ProductItemService productItemService) {
        this.batchRepository = batchRepository;
        this.productItemService = productItemService;
    }

    public Batch findById(Long id) {
        return batchRepository.findById(id).orElse(null);
    }


    public List<Batch> findBatchesByProductId(Long id) {
        List<Batch> batches = batchRepository.findAllByProductId(id);

        if (batches.isEmpty()) {
            return List.of();
        }

        return batches;
    }


    public Batch createBatch(Batch batch) {
        ProductItem productItem = productItemService.getProductItemById(batch.productId());
        if (productItem == null) {
            throw new InvalidParameterException("Product item id not found");
        }
        return batchRepository.save(batch);
    }



    public Integer consumeInventoryByProductId(Long productId, Integer quantityToConsume) {
        List<Batch> batches = batchRepository.findAllByProductIdOrderByValidationDateAsc(productId);

        if (batches.isEmpty()) {
            throw new BatchNotFoundExcption(productId.toString());
        }

        int remainingQuantity = quantityToConsume;
        for (Batch batch : batches) {
            if (remainingQuantity < 0) break;

            int available = batch.quantity();

            if (available >= remainingQuantity) {
                int newQuantity = available - remainingQuantity;
                updateBatchQuantity(batch, newQuantity);

                remainingQuantity = 0;
                break;
            } else {
                updateBatchQuantity(batch, 0);
                remainingQuantity -= available;
            }
        }
        if (remainingQuantity > 0) {
            throw new RuntimeException("Not enough inventory available: " + remainingQuantity + " remaining");
        }

        return quantityToConsume;
    }


    private void updateBatchQuantity(Batch batch, int newQuantity) {
        Batch updated = new Batch(
                batch.id(),
                batch.batchId(),
                batch.productId(),
                batch.cost(),
                newQuantity,
                batch.validationDate(),
                batch.createdAt(),
                LocalDateTime.now()
        );

        batchRepository.save(updated);
    }


}
