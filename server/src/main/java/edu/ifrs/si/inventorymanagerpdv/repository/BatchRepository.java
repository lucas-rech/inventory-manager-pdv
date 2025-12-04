package edu.ifrs.si.inventorymanagerpdv.repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;

import edu.ifrs.si.inventorymanagerpdv.model.Batch;

public interface BatchRepository extends CrudRepository<Batch, Long>, PagingAndSortingRepository<Batch, Long>{
    
    List<Batch> findAllByProductId(Long id);
    List<Batch> findAllByProductIdOrderByValidationDateAsc(Long productId);

}
