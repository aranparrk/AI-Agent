package com.human.mini_prj.security;

import com.human.mini_prj.constant.Authority;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.io.Encoders;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class TokenProviderTest {
    @Test
    void verifiesSignatureExpirationAndTokenType() {
        String secret = Encoders.BASE64.encode(Jwts.SIG.HS512.key().build().getEncoded());
        var provider = new TokenProvider(secret, 3600000, 86400000);
        var pair = provider.createToken("member@example.com", Authority.ROLE_USER);
        assertTrue(provider.validate(pair.accessToken(), TokenProvider.ACCESS));
        assertTrue(provider.validate(pair.refreshToken(), TokenProvider.REFRESH));
        assertFalse(provider.validate(pair.refreshToken(), TokenProvider.ACCESS));
        assertFalse(provider.validate(pair.accessToken(), TokenProvider.REFRESH));
        assertEquals("member@example.com", provider.getAuthentication(pair.accessToken()).getName());
        assertEquals("member@example.com", provider.getEmail(pair.refreshToken()));
        assertNotEquals(pair.refreshToken(),
                provider.createToken("member@example.com", Authority.ROLE_USER).refreshToken());

        var expired = new TokenProvider(secret, -60000, -60000)
                .createToken("member@example.com", Authority.ROLE_USER);
        assertFalse(provider.validate(expired.accessToken(), TokenProvider.ACCESS));
        assertFalse(provider.validate(expired.refreshToken(), TokenProvider.REFRESH));
        assertFalse(provider.validate("invalid", TokenProvider.ACCESS));
        assertFalse(provider.validate(null, TokenProvider.REFRESH));
        String otherSecret = Encoders.BASE64.encode(Jwts.SIG.HS512.key().build().getEncoded());
        var other = new TokenProvider(otherSecret, 3600000, 86400000)
                .createToken("member@example.com", Authority.ROLE_USER);
        assertFalse(provider.validate(other.accessToken(), TokenProvider.ACCESS));
        assertFalse(provider.validate(other.refreshToken(), TokenProvider.REFRESH));
    }
}
