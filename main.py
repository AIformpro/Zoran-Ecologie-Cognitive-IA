import math

def pixel_score(text: str) -> float:
    """
    Calcule un PixelScore cognitif simple.
    Score = utilité perçue / (utilité + déchets sémantiques).
    Ici, on approxime :
    - mots uniques = signal
    - répétitions inutiles = bruit
    """
    words = text.split()
    unique = len(set(words))
    total = len(words)
    if total == 0:
        return 0.0
    signal = unique
    noise = total - unique
    score = signal / (signal + noise + 1e-9)
    return round(score, 3)

if __name__ == "__main__":
    sample = "AI AI AI generates value with redundancy redundancy value."
    print("Texte :", sample)
    print("PixelScore cognitif :", pixel_score(sample))
