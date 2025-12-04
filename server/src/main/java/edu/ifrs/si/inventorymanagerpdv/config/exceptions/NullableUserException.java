package edu.ifrs.si.inventorymanagerpdv.config.exceptions;

public class NullableUserException extends RuntimeException {
    public NullableUserException(String message) {
        super("Nullable user: " + message);
    }
}
