package edu.ifrs.si.inventorymanagerpdv.service;

import java.time.LocalDateTime;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import edu.ifrs.si.inventorymanagerpdv.config.exceptions.NullableUserException;
import edu.ifrs.si.inventorymanagerpdv.config.exceptions.UsernameExistsException;
import edu.ifrs.si.inventorymanagerpdv.model.User;
import edu.ifrs.si.inventorymanagerpdv.repository.UserRepository;

@Service
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
    }

    public User findById(Long id) {
        if (id == null) {
            throw new NullableUserException("id is null");
        }

        return userRepository.findById(id).orElse(null);
    }

    public User create(User newUser) {
        if (newUser == null) {
            throw new NullableUserException("creating newUser is null");
        }
        if (userRepository.findByUsername(newUser.username()) != null) {
            throw new UsernameExistsException(newUser.username());
        }
        User createdUser = new User(
                null,
                newUser.name(),
                newUser.username(),
                newUser.phoneNumber(),
                newUser.role(),
                passwordEncoder.encode(newUser.password()),
                LocalDateTime.now().withNano(0),
                LocalDateTime.now().withNano(0),
                false
        );

        return userRepository.save(createdUser);
    }

}
