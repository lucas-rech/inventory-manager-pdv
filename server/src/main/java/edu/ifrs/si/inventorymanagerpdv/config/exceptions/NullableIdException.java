package edu.ifrs.si.inventorymanagerpdv.config.exceptions;

public class NullableIdException extends RuntimeException {
    public NullableIdException() {
        super("Id cannot be null)");
    }
}
