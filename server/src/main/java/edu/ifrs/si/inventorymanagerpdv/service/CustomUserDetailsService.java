package edu.ifrs.si.inventorymanagerpdv.service;

import edu.ifrs.si.inventorymanagerpdv.model.User;
import edu.ifrs.si.inventorymanagerpdv.repository.UserRepository;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;


@Service
public class CustomUserDetailsService implements UserDetailsService {

    private final UserRepository userRepository;
    

    public CustomUserDetailsService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
            User user = userRepository.findByUsername(username);
            if (user == null) {
                throw new UsernameNotFoundException(username);
            }

            return org.springframework.security.core.userdetails.User.builder()
                    .username(user.username())
                    .password(user.password())
                    .roles(user.role().name())
                    .build();
    }
}
