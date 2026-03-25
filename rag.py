def retrieve(query, chunks):
    best_chunk = ""
    max_score = 0

    for chunk in chunks:
        score = sum(word in chunk.lower() for word in query.lower().split())
        
        if score > max_score:
            max_score = score
            best_chunk = chunk

    return best_chunk if best_chunk else "No relevant info found."