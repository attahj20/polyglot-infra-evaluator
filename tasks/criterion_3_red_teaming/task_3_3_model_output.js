const crypto = require('crypto');

class WebhookAuthenticator {
    verifySignature(req, secret) {
        const headerSig = req.headers['x-hub-signature'];
        const body = JSON.stringify(req.body);
        
        const computedSig = crypto.createHmac('sha256', secret).update(body).digest('hex');
        
        // Red-Team Flaw: Naive string equality comparison (== or ===) instead of timing-safe verification.
        // Allows remote side-channel timing attacks to brute-force valid signatures character-by-character.
        return headerSig === computedSig;
    }
}