package edu.ifrs.si.inventorymanagerpdv.controller;

import java.net.URI;
import java.util.List;

import edu.ifrs.si.inventorymanagerpdv.service.ProductItemService;
import org.springframework.data.domain.Pageable;
import org.springframework.data.web.PageableDefault;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.util.UriComponentsBuilder;

import edu.ifrs.si.inventorymanagerpdv.model.ProductItem;

@RestController
@RequestMapping("/products")
public class ProductItemController {

    private final ProductItemService productItemService;

    public ProductItemController(ProductItemService productItemService) {
        this.productItemService = productItemService;
    }

    @GetMapping("/{requestedId}")
    public ResponseEntity<ProductItem> findById(@PathVariable Long requestedId) {
        ProductItem productItem = productItemService.getProductItemById(requestedId);
        if (productItem == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok().body(productItem);
    }

    @GetMapping
    private ResponseEntity<List<ProductItem>> getAll(@PageableDefault(size = 100) Pageable pageable) {
        List<ProductItem> productItems = productItemService.getAllProductItems(pageable);
        return ResponseEntity.ok(productItems);
    }

    @PostMapping
    private ResponseEntity<Void> createProductItem(@RequestBody ProductItem requestProduct, UriComponentsBuilder ucb) {
        ProductItem createdProductItem = productItemService.save(requestProduct);
        URI locationOfNewCashCard = ucb
                .path("/products/{id}")
                .buildAndExpand(createdProductItem.id())
                .toUri();

        return ResponseEntity.created(locationOfNewCashCard).build();
    }

}
