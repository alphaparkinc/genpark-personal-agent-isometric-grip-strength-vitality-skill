# -*- coding: utf-8 -*-
"""Isometric Grip Strength & Vitality Sentinel for GenPark Personal Agent."""
import json
from typing import Dict, Any

class IsometricGripStrengthVitalitySentinel:
    @staticmethod
    def assess_grip_strength_vitality_index(grip_dominant_kg: float, chronological_age: int, gender: str, grip_non_dominant_kg: float = 0.0) -> Dict[str, Any]:
        # Reference normative values for healthy 30yo: Male ~50kg, Female ~32kg
        base_norm = 50.0 if gender.lower() == "male" else 32.0
        age_decay_factor = max(0.6, 1.0 - max(0, chronological_age - 30) * 0.008)
        expected_grip = round(base_norm * age_decay_factor, 1)
        
        strength_ratio = grip_dominant_kg / max(1.0, expected_grip)
        bio_age_delta = round((1.0 - strength_ratio) * 15.0, 1)
        biological_vitality_age = round(chronological_age + bio_age_delta, 1)
        
        if strength_ratio >= 1.15:
            tier = "ELITE_NEUROMUSCULAR_LONGEVITY"
            hazard_ratio = 0.68  # 32% reduced all-cause mortality
        elif strength_ratio >= 0.90:
            tier = "OPTIMAL_FUNCTIONAL_VITALITY"
            hazard_ratio = 1.0
        else:
            tier = "SARCOPENIA_FRAILTY_RISK"
            hazard_ratio = 1.45
            
        return {
            "dominant_grip_kg": grip_dominant_kg,
            "cohort_expected_grip_kg": expected_grip,
            "biological_vitality_age": biological_vitality_age,
            "vitality_tier": tier,
            "all_cause_mortality_hazard_ratio": hazard_ratio
        }

    @staticmethod
    def synthesize_neuromuscular_grip_protocol(current_dominant_kg: float, target_tier: str = "ELITE") -> Dict[str, Any]:
        return {
            "prescribed_interventions": [
                "Heavy Farmer's Walks: 3 sets x 40m with 50% bodyweight per hand twice weekly",
                "Dead hangs from pull-up bar: 3 x 60s max accumulated duration",
                "Reverse wrist curls and finger extension rubber band training to balance extensor tendons"
            ],
            "progressive_target_kg": round(current_dominant_kg * 1.15, 1),
            "expected_timeline_weeks": 8
        }
