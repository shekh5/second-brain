---
type: concept
tags: [system-design, caching, networking]
sources: [caching-basics]
created: 2026-11-14
updated: 2026-11-14
---

# CDN (Content Delivery Network)

**In one line:** a network of servers around the world that keep copies of static files close to users.

## How it works
```
user in Jaipur ──► CDN edge in Mumbai (hit ⚡) 
                         │ miss
                         ▼
                   origin server (e.g. in US)
```
A CDN is [[caching]] at the network edge, for files like images, video, CSS and JS. (src: [[caching-basics]])

## Why it matters
- Lower latency: data travels a shorter distance.
- Less load and bandwidth on your origin servers.
(note: general knowledge, not from a source)

## Trade-offs
| Pro | Con |
|---|---|
| fast global delivery | costs money per GB |
| absorbs traffic spikes | purging stale files takes time ([[cache-invalidation]]) |

## Real-world examples
- Netflix Open Connect: CDN boxes placed inside ISPs to cache video. (src: [[caching-basics]])
- Cloudflare, Akamai, AWS CloudFront. (note: general knowledge, not from a source)

## Sources
- [[caching-basics]]
