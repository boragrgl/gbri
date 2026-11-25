# Faz 0 · Yapay zekâ testi (GitHub Models ve Gemini)

Denenenler: github:openai/gpt-4.1, gemini:gemini-omni-1.2-flash

| Model | Kaynak | Sonuç | Süre (sn) | Gönderilen kr | Token (girdi/çıktı) | Teyitli alıntı birebir | Önem | Statü |
|---|---|---|---|---|---|---|---|---|
| github:openai/gpt-4.1 | BIS/BCBS | HATA | 0.2 | 2549 | -/- | -/- | - | - |
| github:openai/gpt-4.1 | ECB | HATA | 0.3 | 9000 | -/- | -/- | - | - |
| github:openai/gpt-4.1 | Resmi Gazete | HATA | 0.2 | 9000 | -/- | -/- | - | - |
| gemini:gemini-omni-1.2-flash | BIS/BCBS | HATA | 0.1 | 2549 | -/- | -/- | - | - |
| gemini:gemini-omni-1.2-flash | ECB | HATA | 0.1 | 40000 | -/- | -/- | - | - |
| gemini:gemini-omni-1.2-flash | Resmi Gazete | HATA | 0.1 | 40000 | -/- | -/- | - | - |

## github:openai/gpt-4.1 · BIS/BCBS
Belge: Basel Committee publishes more details on the 2026 assessment of global systemically important banks — https://www.bis.org/media-releases/20261125-basel-committee-publishes-more-details-2026-assessment-global-systemically-important-banks

```json
JSON degil: HTTP 200 text/plain url=https://models.github.ai/inference/chat/completions govde=b'OK\r\n'
```

## github:openai/gpt-4.1 · ECB
Belge: Introduction to the ECB Token Reference Model - a framework for standardisation discussions — https://www.ecb.europa.eu//pub/pdf/other/ecb.introproposalTRM2026.en.pdf

```json
JSON degil: HTTP 200 text/plain url=https://models.github.ai/inference/chat/completions govde=b'OK\r\n'
```

## github:openai/gpt-4.1 · Resmi Gazete
Belge: Resmi Gazete - gunun icindekiler — https://www.resmigazete.gov.tr/

```json
JSON degil: HTTP 200 text/plain url=https://models.github.ai/inference/chat/completions govde=b'OK\r\n'
```

## gemini:gemini-omni-1.2-flash · BIS/BCBS
Belge: Basel Committee publishes more details on the 2026 assessment of global systemically important banks — https://www.bis.org/media-releases/20261125-basel-committee-publishes-more-details-2026-assessment-global-systemically-important-banks

```json
HTTP 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 0, model
```

## gemini:gemini-omni-1.2-flash · ECB
Belge: Introduction to the ECB Token Reference Model - a framework for standardisation discussions — https://www.ecb.europa.eu//pub/pdf/other/ecb.introproposalTRM2026.en.pdf

```json
HTTP 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 0, model
```

## gemini:gemini-omni-1.2-flash · Resmi Gazete
Belge: Resmi Gazete - gunun icindekiler — https://www.resmigazete.gov.tr/

```json
HTTP 429: {
  "error": {
    "code": 429,
    "message": "You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://aistudio.google.com/docs/rate-limits. To monitor your current usage, head to: https://ai.dev/rate-limit. \n* Quota exceeded for metric: generativelanguage.googleapis.com/generate_content_free_tier_requests, limit: 0, model
```
