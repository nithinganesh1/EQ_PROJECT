from transformers import pipeline
import re

emotion_analyzer = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True,
    framework="pt"
)

EQ_CATEGORIES = [
    "Self Awareness",
    "Emotional Regulation",
    "Conflict Handling",
    "Empathy",
    "Resilience"
]

# Scenario & Questions
def generate_scenario(profession):
    return (
        f"You are working as a {profession}. "
        "A disagreement occurs with a colleague over an urgent deadline. "
        "The colleague insists their approach is correct, and tensions are rising."
    )

def generate_questions():
    return [
        "How do you feel in this situation? What emotions do you notice?",
        "What steps would you take to manage your emotions?",
        "How would you approach resolving this conflict?",
        "How do you understand your colleague's perspective?",
        "How do you stay motivated and handle the pressure?"
    ]

# Emotion weights (higher = better EQ indicator)
EMOTION_WEIGHTS = {
    "anger": 0.2,
    "disgust": 0.3,
    "fear": 0.4,
    "sadness": 0.5,
    "neutral": 0.7,
    "surprise": 0.6,
    "joy": 0.9
}

# EQ keyword signals
EQ_KEYWORDS = {
    "Self Awareness": [
        "i feel", "i realize", "i notice", "aware", "recognize my"
    ],
    "Emotional Regulation": [
        "stay calm", "take a breath", "pause", "control", "manage my"
    ],
    "Conflict Handling": [
        "discuss", "compromise", "solution", "resolve", "communicate", "listen"
    ],
    "Empathy": [
        "their perspective", "understand them", "they might feel", "empathize", "their view"
    ],
    "Resilience": [
        "move forward", "stay focused", "handle pressure", "adapt", "keep going", "overcome"
    ]
}

# Scoring functions
def emotion_score(text):
    """Score based on dominant emotion quality"""
    if not emotion_analyzer:
        return 0.5
    
    try:
        emotions = emotion_analyzer(text)[0]
        # Find the emotion with highest confidence
        dominant = max(emotions, key=lambda x: x["score"])
        return EMOTION_WEIGHTS.get(dominant["label"], 0.5)
    except:
        return 0.5

def keyword_score(text, category):
    """Score based on relevant EQ keywords with word boundaries"""
    text = text.lower()
    hits = 0
    
    for kw in EQ_KEYWORDS[category]:
        # Use word boundaries to avoid partial matches
        if re.search(r'\b' + re.escape(kw), text):
            hits += 1
    
    # Cap at 1.0, each keyword worth 0.25
    return min(hits * 0.25, 1.0)

def depth_score(text):
    """Score based on response thoughtfulness"""
    words = text.split()
    length = len(words)
    
    if length < 10:
        return 0.2  # Too short
    elif length < 25:
        return 0.5  # Brief
    elif length < 60:
        return 0.8  # Good depth
    else:
        return 0.9  # Detailed 

def validate_response(text):
    """Check if response is valid"""
    if not text or len(text.strip()) < 5:
        return False
    if len(text.split()) < 3:
        return False
    return True

def score_response(text, category):
    """
    Calculate final score for a response (0-10 scale)
    Weights: 40% emotion quality, 40% keywords, 20% depth
    """
    if not validate_response(text):
        return 0.0
    
    e = emotion_score(text)
    k = keyword_score(text, category)
    d = depth_score(text)
    
    # Weighted combination
    final_score = (0.4 * e) + (0.4 * k) + (0.2 * d)
    
    # Convert to 0-10 scale
    return round(final_score * 10, 1)


# Final EQ calculation
def calculate_eq(responses):
    """Calculate overall EQ and breakdown by category"""
    if len(responses) != len(EQ_CATEGORIES):
        raise ValueError(f"Expected {len(EQ_CATEGORIES)} responses, got {len(responses)}")
    
    breakdown = {}
    total = 0.0
    
    for category, response in zip(EQ_CATEGORIES, responses):
        score = score_response(response, category)
        breakdown[category] = score
        total += score
    
    overall = round(total / len(EQ_CATEGORIES), 1)
    
    return overall, breakdown

def get_eq_interpretation(score):
    """Provide interpretation of EQ score"""
    if score >= 8.5:
        return "Exceptional - Very high emotional intelligence"
    elif score >= 7.0:
        return "Strong - Well-developed emotional intelligence"
    elif score >= 5.5:
        return "Moderate - Good emotional awareness with room to grow"
    elif score >= 4.0:
        return "Developing - Basic emotional intelligence skills"
    else:
        return "Emerging - Significant opportunity for development"
