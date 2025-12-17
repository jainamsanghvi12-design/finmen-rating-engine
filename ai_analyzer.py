"""AI-Powered Rating Analysis Engine - FINMEN v3"""
from typing import Dict, List, Tuple
import re
from dataclasses import dataclass
from datetime import datetime
import json

@dataclass
class AnalysisResult:
    """Data class for AI analysis results"""
    company: str
    rating: str
    strengths: List[str]
    risks: List[str]
    financial_health: str
    industry_position: str
    ai_recommendation: str
    confidence_score: float
    upgrade_opportunities: List[str]
    downgrade_warnings: List[str]
    key_metrics: Dict
    sentiment_score: float
    timestamp: str

class AIRatingAnalyzer:
    """Advanced AI analyzer for rating rationales"""
    
    def __init__(self):
        self.analysis_cache = {}
        self.rating_scale = {
            'AAA': 10, 'AA+': 9.7, 'AA': 9.5, 'AA-': 9.2,
            'A+': 8.7, 'A': 8.5, 'A-': 8.2,
            'BBB+': 7.2, 'BBB': 7, 'BBB-': 6.8,
            'BB+': 5.7, 'BB': 5.5, 'BB-': 5.2,
            'B+': 4.2, 'B': 4, 'B-': 3.7,
            'CCC': 2, 'CC': 1, 'C': 0.5, 'D': 0
        }
    
    def analyze_rationale(self, company: str, rationale: str, rating: str, agency: str = "") -> AnalysisResult:
        """Main analysis function"""
        return AnalysisResult(
            company=company,
            rating=rating,
            strengths=self._extract_strengths(rationale),
            risks=self._extract_risks(rationale),
            financial_health=self._assess_financial_health(rationale),
            industry_position=self._assess_industry_position(rationale),
            ai_recommendation=self._generate_recommendation(rating, rationale),
            confidence_score=self._calculate_confidence(rationale),
            upgrade_opportunities=self._identify_upgrades(rationale, rating),
            downgrade_warnings=self._identify_downgrades(rationale, rating),
            key_metrics=self._extract_metrics(rationale),
            sentiment_score=self._calculate_sentiment(rationale),
            timestamp=datetime.now().isoformat()
        )
    
    def _extract_strengths(self, rationale: str) -> List[str]:
        """Extract company strengths from rationale"""
        strength_patterns = {
            'Market Position': ['market leader', 'leading position', 'dominant', 'strong brand'],
            'Financial Strength': ['strong financials', 'robust cash flow', 'healthy margins', 'strong EBITDA', 'low leverage'],
            'Growth Trajectory': ['growing', 'expansion', 'scaling', 'strong growth', 'expanding market'],
            'Management Quality': ['experienced management', 'strong management', 'proven track record'],
            'Asset Quality': ['quality assets', 'strong asset base', 'good quality'],
            'Operational Efficiency': ['efficient operations', 'high efficiency', 'operational excellence']
        }
        
        strengths = []
        text_lower = rationale.lower()
        
        for category, keywords in strength_patterns.items():
            for keyword in keywords:
                if keyword in text_lower:
                    if category not in strengths:
                        strengths.append(category)
                    break
        
        return strengths[:6]
    
    def _extract_risks(self, rationale: str) -> List[str]:
        """Extract identified risks from rationale"""
        risk_patterns = {
            'Market Risk': ['market volatility', 'cyclical', 'industry downturn', 'intense competition', 'market share loss'],
            'Financial Risk': ['weak financials', 'high leverage', 'debt burden', 'liquidity concerns', 'margin pressure'],
            'Operational Risk': ['operational challenges', 'execution risk', 'supply chain', 'capacity constraints'],
            'Regulatory Risk': ['regulatory changes', 'compliance', 'regulatory pressure', 'policy risk'],
            'Management Risk': ['management changes', 'key person dependency', 'governance concerns'],
            'Technology Risk': ['technology disruption', 'obsolescence', 'digital transformation']
        }
        
        risks = []
        text_lower = rationale.lower()
        
        for category, keywords in risk_patterns.items():
            for keyword in keywords:
                if keyword in text_lower:
                    if category not in risks:
                        risks.append(category)
                    break
        
        return risks[:6]
    
    def _assess_financial_health(self, rationale: str) -> str:
        """Rate financial health from Strong to Weak"""
        text_lower = rationale.lower()
        
        strong_indicators = ['strong', 'healthy', 'robust', 'excellent', 'solid']
        moderate_indicators = ['moderate', 'adequate', 'stable', 'fair']
        weak_indicators = ['weak', 'stressed', 'deteriorating', 'challenging', 'declining']
        
        strong_count = sum(1 for ind in strong_indicators if ind in text_lower)
        weak_count = sum(1 for ind in weak_indicators if ind in text_lower)
        
        if strong_count >= 3:
            return 'Strong'
        elif weak_count >= 2:
            return 'Weak'
        else:
            return 'Moderate'
    
    def _assess_industry_position(self, rationale: str) -> str:
        """Assess company's position in industry"""
        text_lower = rationale.lower()
        
        if any(term in text_lower for term in ['market leader', 'leading player', 'dominant', '#1', 'number 1']):
            return 'Market Leader'
        elif any(term in text_lower for term in ['competitive', 'strong position', 'established']):
            return 'Strong Competitive Position'
        elif any(term in text_lower for term in ['niche', 'specialized', 'regional']):
            return 'Niche/Regional Player'
        else:
            return 'Stable Market Position'
    
    def _generate_recommendation(self, rating: str, rationale: str) -> str:
        """Generate AI investment recommendation"""
        score = self.rating_scale.get(rating, 5)
        text_lower = rationale.lower()
        
        # Check for upgrade triggers
        upgrade_triggers = ['improving', 'strengthening', 'recovery', 'growth acceleration', 'market expansion']
        downgrade_triggers = ['deteriorating', 'challenging', 'weakness', 'headwinds', 'margin compression']
        
        upgrade_count = sum(1 for trigger in upgrade_triggers if trigger in text_lower)
        downgrade_count = sum(1 for trigger in downgrade_triggers if trigger in text_lower)
        
        if score >= 8.5:
            if upgrade_count > 0:
                return '🟢 BUY - AAA/AA rated, strong fundamentals with improvement potential'
            return '🟢 HOLD - Maintain, excellent credit quality'
        elif score >= 7.5:
            if downgrade_count > 0:
                return '🟡 HOLD - Monitor, good credit but watch for headwinds'
            return '🟢 BUY - Strong credit quality, good value'
        elif score >= 6:
            if upgrade_count > 1:
                return '🟡 HOLD - Monitor for upgrade potential'
            return '🟡 HOLD - Moderate credit quality'
        else:
            if downgrade_count > downgrade_count:
                return '🔴 SELL - Watch for further downgrades'
            return '🟡 CAUTION - Higher risk, close monitoring required'
    
    def _calculate_confidence(self, rationale: str) -> float:
        """Calculate confidence score (0-1)"""
        if len(rationale) < 50:
            return 0.6
        elif len(rationale) < 200:
            return 0.75
        elif len(rationale) < 500:
            return 0.85
        else:
            return 0.92
    
    def _identify_upgrades(self, rationale: str, current_rating: str) -> List[str]:
        """Identify potential upgrade triggers"""
        opportunities = []
        text_lower = rationale.lower()
        
        if any(term in text_lower for term in ['improving', 'strengthening', 'recovery']):
            opportunities.append('Improving Fundamentals')
        if any(term in text_lower for term in ['margin expansion', 'deleveraging', 'debt reduction']):
            opportunities.append('Improving Leverage Metrics')
        if any(term in text_lower for term in ['market growth', 'expansion', 'new projects']):
            opportunities.append('Revenue/Market Expansion')
        if any(term in text_lower for term in ['cost reduction', 'efficiency', 'optimization']):
            opportunities.append('Operational Improvements')
        if any(term in text_lower for term in ['cash generation', 'strong fcf', 'positive cash flow']):
            opportunities.append('Strong Cash Generation')
        
        return opportunities
    
    def _identify_downgrades(self, rationale: str, current_rating: str) -> List[str]:
        """Identify potential downgrade risks"""
        warnings = []
        text_lower = rationale.lower()
        
        if any(term in text_lower for term in ['deteriorating', 'challenging', 'headwinds']):
            warnings.append('Deteriorating Fundamentals')
        if any(term in text_lower for term in ['leverage increase', 'debt increase', 'rising debt']):
            warnings.append('Leverage Deterioration')
        if any(term in text_lower for term in ['market decline', 'volume decline', 'revenue decline']):
            warnings.append('Revenue/Volume Pressure')
        if any(term in text_lower for term in ['margin compression', 'ebitda decline']):
            warnings.append('Margin Compression')
        if any(term in text_lower for term in ['liquidity', 'refinancing', 'covenant']):
            warnings.append('Liquidity/Refinancing Risk')
        
        return warnings
    
    def _extract_metrics(self, rationale: str) -> Dict:
        """Extract financial metrics mentioned in rationale"""
        metrics = {}
        
        # Extract numbers that look like percentages
        percentage_pattern = r'(\d+\.?\d*)\s*%'
        percentages = re.findall(percentage_pattern, rationale)
        if percentages:
            metrics['mentions_percentages'] = len(percentages)
        
        # Extract ratios
        ratio_keywords = ['leverage', 'roe', 'roa', 'debt', 'equity', 'ratio', 'multiple']
        for keyword in ratio_keywords:
            if keyword in rationale.lower():
                metrics[keyword] = True
        
        return metrics
    
    def _calculate_sentiment(self, rationale: str) -> float:
        """Calculate sentiment score (-1 to 1)"""
        text_lower = rationale.lower()
        
        positive_words = ['strong', 'excellent', 'robust', 'improving', 'growth', 'solid', 'good']
        negative_words = ['weak', 'poor', 'declining', 'challenging', 'risk', 'pressure', 'concern']
        
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)
        
        total = pos_count + neg_count
        if total == 0:
            return 0.0
        
        return (pos_count - neg_count) / total
    
    def batch_analyze(self, companies_data: List[Dict]) -> List[AnalysisResult]:
        """Analyze multiple companies at once"""
        results = []
        for company_data in companies_data:
            result = self.analyze_rationale(
                company=company_data.get('company'),
                rationale=company_data.get('rationale'),
                rating=company_data.get('rating'),
                agency=company_data.get('agency', '')
            )
            results.append(result)
        return results
    
    def to_dict(self, result: AnalysisResult) -> Dict:
        """Convert analysis result to dictionary for storage"""
        return {
            'company': result.company,
            'rating': result.rating,
            'strengths': result.strengths,
            'risks': result.risks,
            'financial_health': result.financial_health,
            'industry_position': result.industry_position,
            'ai_recommendation': result.ai_recommendation,
            'confidence_score': result.confidence_score,
            'upgrade_opportunities': result.upgrade_opportunities,
            'downgrade_warnings': result.downgrade_warnings,
            'key_metrics': result.key_metrics,
            'sentiment_score': result.sentiment_score,
            'timestamp': result.timestamp
        }
