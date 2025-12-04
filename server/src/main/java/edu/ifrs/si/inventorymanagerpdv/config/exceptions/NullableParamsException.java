package edu.ifrs.si.inventorymanagerpdv.config.exceptions;

public class NullableParamsException extends RuntimeException {
    public NullableParamsException(String message) {
        super("NullableParamsException: " + message);
    }
}
