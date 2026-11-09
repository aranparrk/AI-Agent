package com.human.mini_prj.security;

import com.human.mini_prj.constant.Authority;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.io.Encoders;
import org.junit.jupiter.api.Test;

import java.util.Date;

import static org.junit.jupiter.api.Assertions.*;

class TokenProviderTest {
    @Test
    void verifiesSignatureExpirationAndRequiredClaims() {
        var key = Jwts.SIG.HS512.key().build();
        String secret = Encoders.BASE64.encode(key.getEncoded());
        var provider = new TokenProvider(secret, 3600000);
        String valid = provider.createToken("member@example.com", Authority.ROLE_USER).accessToken();
        assertTrue(provider.validate(valid));
        assertEquals("member@example.com", provider.getAuthentication(valid).getName());
        assertFalse(provider.validate(new TokenProvider(secret, -60000)
                .createToken("member@example.com", Authority.ROLE_USER).accessToken()));
        assertFalse(provider.validate(valid.substring(0, valid.lastIndexOf('.') + 1) + "AAAA"));
        assertFalse(provider.validate("invalid"));
        assertFalse(provider.validate(null));
        String otherSecret = Encoders.BASE64.encode(Jwts.SIG.HS512.key().build().getEncoded());
        assertFalse(provider.validate(new TokenProvider(otherSecret, 3600000)
                .createToken("member@example.com", Authority.ROLE_USER).accessToken()));
        assertFalse(provider.validate(Jwts.builder().subject("member@example.com")
                .expiration(new Date(System.currentTimeMillis() + 60000)).signWith(key).compact()));
        assertFalse(provider.validate(Jwts.builder().claim("auth", "ROLE_USER")
                .expiration(new Date(System.currentTimeMillis() + 60000)).signWith(key).compact()));
        assertFalse(provider.validate(Jwts.builder().subject("member@example.com").claim("auth", "UNKNOWN")
                .expiration(new Date(System.currentTimeMillis() + 60000)).signWith(key).compact()));
        assertFalse(provider.validate(Jwts.builder().subject("member@example.com").claim("auth", "ROLE_USER")
                .signWith(key).compact()));
        assertFalse(provider.validate(Jwts.builder().subject("member@example.com").claim("auth", 123)
                .expiration(new Date(System.currentTimeMillis() + 60000)).signWith(key).compact()));
    }
}
