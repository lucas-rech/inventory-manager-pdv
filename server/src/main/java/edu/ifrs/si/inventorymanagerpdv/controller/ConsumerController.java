package edu.ifrs.si.inventorymanagerpdv.controller;

import edu.ifrs.si.inventorymanagerpdv.model.Consumer;
import edu.ifrs.si.inventorymanagerpdv.model.dto.CreateConsumerDTO;
import edu.ifrs.si.inventorymanagerpdv.service.ConsumerService;
import org.springframework.data.domain.Pageable;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;
import java.util.List;

@RestController
@RequestMapping("/consumers")
public class ConsumerController {

    private final ConsumerService consumerService;

    public ConsumerController(ConsumerService consumerService) {
        this.consumerService = consumerService;
    }



    @GetMapping
    public ResponseEntity<List<Consumer>> getAllConsumers(Pageable pageable) {
        List<Consumer> response = consumerService.getAllConsumers(pageable);

        return ResponseEntity.ok(response);
    }


    @GetMapping("/{requestedId}")
    public ResponseEntity<Consumer> getConsumerById(@PathVariable  Long requestedId) {
        Consumer response = consumerService.getConsumerById(requestedId);

        if (response == null) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(response);
    }


    @PostMapping
    public ResponseEntity<Void> createConsumer(@RequestBody CreateConsumerDTO consumer, UriComponentsBuilder ucb) {
        Consumer createdConsumer = consumerService.save(consumer);
        URI locationOfNewConsumer = ucb
                .path("/consumers/{id}")
                .buildAndExpand(createdConsumer.id())
                .toUri();

        return ResponseEntity.created(locationOfNewConsumer).build();
    }
}
