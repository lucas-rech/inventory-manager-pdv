package edu.ifrs.si.inventorymanagerpdv.repository;

import edu.ifrs.si.inventorymanagerpdv.model.User;
import org.springframework.data.repository.CrudRepository;

public interface UserRepository extends CrudRepository<User, Long> {
    public User findByUsername(String username);
}
