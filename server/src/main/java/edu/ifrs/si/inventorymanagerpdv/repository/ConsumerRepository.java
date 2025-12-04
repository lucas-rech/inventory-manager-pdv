package edu.ifrs.si.inventorymanagerpdv.repository;

import edu.ifrs.si.inventorymanagerpdv.model.Consumer;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;


public interface ConsumerRepository extends CrudRepository<Consumer, Long>, PagingAndSortingRepository<Consumer, Long> {
}
