package edu.ifrs.si.inventorymanagerpdv.config.exceptions;

public class BatchNotFoundExcption extends RuntimeException {
    public BatchNotFoundExcption(String message) {
        super(
                "Batch not found: " + message
        );
    }
}
