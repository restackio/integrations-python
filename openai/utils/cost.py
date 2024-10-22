from dataclasses import dataclass

@dataclass
class TokensCount:
    input: int
    output: int

@dataclass
class Price:
    input: float
    output: float

def openai_cost(tokens_count: TokensCount, price: Price) -> float:
    cost = (tokens_count.input * price.input) + (tokens_count.output * price.output)
    return cost
