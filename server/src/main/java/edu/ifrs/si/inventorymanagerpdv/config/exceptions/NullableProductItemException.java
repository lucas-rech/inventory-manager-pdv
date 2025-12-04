package edu.ifrs.si.inventorymanagerpdv.config.exceptions;

public class NullableProductItemException extends RuntimeException {
    public NullableProductItemException() {
        super("ProductItem is null");
    }
}
