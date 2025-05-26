export default defineEventHandler((event) => {
    let data = Array(15).fill().map((_, i) => ({
        "source_url": "https://github.com/Abdur-Rahim-sheikh",
        "country_code": "bn",
        "source_id": "bbc-news",
        "title": `the daily kand #${i + 1}`,
        "summary": "Why people work like hellWhy people work like hell ".repeat(i),
        "source_name": "kaler kantho",
        "publication_date": "2025-05-25",
        "thumbnail_url": "https://imgs.search.brave.com/9Heay88JqqUoqwWTX9-Dc7-4b6nI01G4XW3sQhoCE_w/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMudmVjdGVlenku/Y29tL3N5c3RlbS9y/ZXNvdXJjZXMvdGh1/bWJuYWlscy8wMTEv/NTY4LzEwOS9zbWFs/bC9idXNpbmVzcy1u/ZXdzcGFwZXItaXNv/bGF0ZWQtb24td2hp/dGUtYmFja2dyb3Vu/ZC1kYWlseS1uZXdz/cGFwZXItbW9jay11/cC1jb25jZXB0LXBo/b3RvLmpwZw"
    }))
    return data
})