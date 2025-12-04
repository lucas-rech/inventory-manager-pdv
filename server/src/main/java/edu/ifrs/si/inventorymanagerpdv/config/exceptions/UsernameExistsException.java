package edu.ifrs.si.inventorymanagerpdv.config.exceptions;

public class UsernameExistsException extends RuntimeException {
    public UsernameExistsException(String message) {
        super("Username with this name already exists: " + message);
    }
}
