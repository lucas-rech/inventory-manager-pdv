package edu.ifrs.si.inventorymanagerpdv.service;

import edu.ifrs.si.inventorymanagerpdv.config.exceptions.NullableIdException;
import edu.ifrs.si.inventorymanagerpdv.config.exceptions.NullableParamsException;
import edu.ifrs.si.inventorymanagerpdv.config.exceptions.NullableProductItemException;
import edu.ifrs.si.inventorymanagerpdv.model.ProductItem;
import edu.ifrs.si.inventorymanagerpdv.repository.ProductItemRepository;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
public class ProductItemService {

    private final ProductItemRepository productItemRepository;

    ProductItemService(ProductItemRepository productItemRepository) {
        this.productItemRepository = productItemRepository;
    }

    public ProductItem getProductItemById(Long id) {
        if (id == null) {
            throw new NullableIdException();
        }
        Optional<ProductItem> productItem = productItemRepository.findById(id);
        return productItem.orElse(null);
    }

    public List<ProductItem> getAllProductItems(Pageable pageRequest) {
        return productItemRepository.findAll(
                PageRequest.of(
                        pageRequest.getPageNumber(),
                        pageRequest.getPageSize(),
                        pageRequest.getSortOr(Sort.by(Sort.Direction.ASC, "id"))
                )
        ).getContent();
    }

    public ProductItem save(ProductItem productItem) {
        if (productItem == null) {
            throw new NullableProductItemException();
        } else if (productItem.gtin() == null || productItem.name() == null|| productItem.price() == null) {
            throw new NullableParamsException(
                    productItem.gtin() + " " + productItem.name() + " " + productItem.price()
            );
        }

        ProductItem itemToSave = new ProductItem(
                null,
                productItem.name(),
                productItem.description(),
                productItem.gtin(),
                productItem.ncm(),
                productItem.price(),
                productItem.cost(),
                LocalDateTime.now(),
                LocalDateTime.now()
        );

        return productItemRepository.save(itemToSave);
    }




}
