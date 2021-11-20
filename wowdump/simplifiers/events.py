# simplify event identifiers in events in m2 files
import argparse
import logging
from typing import Any, List

from . import SimplifierUncompiled


def simplify_events(d: Any, _parent: Any, _args: argparse.Namespace) -> str:
    logger = logging.getLogger("simplify")
    logger.debug("using events simplifier")

    if d in m2_events:
        return f"{d}  # {m2_events[d]}"
    else:
        return str(d)


m2_events = {
    "$AH0": "PlaySoundKit (customAttack[0])",
    "$AH1": "PlaySoundKit (customAttack[1])",
    "$AH2": "PlaySoundKit (customAttack[2])",
    "$AH3": "PlaySoundKit (customAttack[3])",
    "$BMD": "BowMissleDestination",
    "$ALT": "Anim Swap Event",
    "$BL0": "Backwards Footstep Anim Event Hit L",
    "$BL1": "Backwards Footstep Anim Event Hit L",
    "$BL2": "Backwards Footstep Anim Event Hit L",
    "$BL3": "Backwards Footstep Anim Event Hit L",
    "$BR0": "Backwards Footstep Anim Event Hit R",
    "$BR1": "Backwards Footstep Anim Event Hit R",
    "$BR2": "Backwards Footstep Anim Event Hit R",
    "$BR3": "Backwards Footstep Anim Event Hit R",
    # soundEffect ID is defined by CreatureSoundDatarec::m_birthSoundID
    "$BRT": "PlaySoundKit (birth)",
    "$BTH": "Breath",
    "$BWP": "PlayRangedItemPull (Bow Pull)",
    "$BWR": "BowRelease",
    "$CAH": "Attack Hold",
    # Only z is used. Non-animated. Not used if $CMA
    "$CFM": "CGCamera::UpdateMountHeightOrOffset",
    "$CMA": "CGCamera::UpdateMountHeightOrOffset",  # Position for camera
    # parry, anims, depending on some state, also some callback which might do more
    "$CPP": "PlayCombatActionAnimKit",
    "$CSD": "PlayEmoteSound",  # data = soundEntryId
    "$CSL": "release missles if pending (L)",
    "$CSR": "release missles if pending (R)",
    # sound played depends on CGUnit_C::GetWeaponSwingType
    "$CSS": "PlayWeaponSwooshSound",
    "$CST": "release missles if pending",
    "$DSE": "DestroyEmitter",
    "$DSO": "DoodadSoundOneShot",
    "$DTH": "DeathThud + LootEffect",
    "$EAC": "object package state enter 3, exit 2, 4, 5",
    "$EDC": "object package state enter 5, exit 3, 4, 2",
    "$EMV": "object package state enter 4, exit 3, 2, 5",
    # soundEffect ID is implicit by currently played emote
    "$ESD": "PlayEmoteStateSound",
    "$EWT": "object package state enter 2, exit 3, 4, 5",
    "$FD0": "PlayFidgetSound[0]",  # from CreatureSoundDataRec::m_soundFidget
    "$FD1": "PlayFidgetSound[1]",
    "$FD2": "PlayFidgetSound[2]",
    "$FD3": "PlayFidgetSound[3]",
    "$FD4": "PlayFidgetSound[4]",
    "$FD5": "PlayFidgetSound[5]",
    "$FD6": "PlayFidgetSound[6]",
    "$FD7": "PlayFidgetSound[7]",
    "$FD8": "PlayFidgetSound[8]",
    "$FD9": "PlayFidgetSound[9]",
    # soundEffect ID is defined by CreatureSoundDataRec::m_soundStandID
    "$FDX": "PlayUnitSound(stand)",
    "$FL0": "FootstepAnimEventHitL[0]",
    "$FL1": "FootstepAnimEventHitL[1]",
    "$FL2": "FootstepAnimEventHitL[2]",
    "$FL3": "FootstepAnimEventHitL[3]",
    "$FR0": "FootstepAnimEventHitR[0]",
    "$FR1": "FootstepAnimEventHitR[1]",
    "$FR2": "FootstepAnimEventHitR[2]",
    "$FR3": "FootstepAnimEventHitR[3]",
    "$FSD": "HandleFootfallAnimEvent",
    # soundEffect ID is defined by GameObjectDisplayInfoRec::m_Sound[x + 6] ({Custom0, Custom1, Custom2, Custom3})
    "$GC0": "GameObject_C_PlayAnimatedSound[0]",
    "$GC1": "GameObject_C_PlayAnimatedSound[1]",
    "$GC2": "GameObject_C_PlayAnimatedSound[2]",
    "$GC3": "GameObject_C_PlayAnimatedSound[3]",
    # soundEffect ID is defined by GameObjectDisplayInfoRec::m_Sound[x] ({Stand, Open, Loop, Close, Destroy, Opened})
    "$GO0": "GameObject_C_PlayAnimatedSound2[0]",
    "$GO1": "GameObject_C_PlayAnimatedSound2[1]",
    "$GO2": "GameObject_C_PlayAnimatedSound2[2]",
    "$GO3": "GameObject_C_PlayAnimatedSound2[3]",
    "$GO4": "GameObject_C_PlayAnimatedSound2[4]",
    "$GO5": "GameObject_C_PlayAnimatedSound2[5]",
    "$HIT": "PlayWoundAnimKit",  # soundEntryId depends on SpellVisualKit
    "$RL0": "FootstepAnimEventHitL[0] (running)",
    "$RL1": "FootstepAnimEventHitL[1] (running)",
    "$RL2": "FootstepAnimEventHitL[2] (running)",
    "$RL3": "FootstepAnimEventHitL[3] (running)",
    "$RR0": "FootstepAnimEventHitR[0] (running)",
    "$RR1": "FootstepAnimEventHitR[1] (running)",
    "$RR2": "FootstepAnimEventHitR[2] (running)",
    "$RR3": "FootstepAnimEventHitR[3] (running)",
    # soundEffect ID is defined by CreatureSoundDataRec::m_spellCastDirectedSoundID
    "$SCD": "PlaySoundKit (spellCastDirectedSound)",
    "$SHK": "AddShake",  # arg is spellEffectCameraShakesID
    "$SHL": "ExchangeSheathedWeaponL",
    "$SHR": "ExchangeSheathedWeaponR",
    "$SL0": "FootstepAnimEventHitL[0]",
    "$SL1": "FootstepAnimEventHitL[1]",
    "$SL2": "FootstepAnimEventHitL[2]",
    "$SL3": "FootstepAnimEventHitL[3]",
    # soundEffect ID is defined by CreatureSoundDatarec::m_submergedSoundID
    "$SMD": "PlaySoundKit (submerged)",
    # soundEffect ID is defined by CreatureSoundDatarec::m_submergeSoundID
    "$SMG": "PlaySoundKit (submerge)",
    "$SND": "PlaySoundKit (custom)",  # arg is soundEntryId
    "$SR0": "FootstepAnimEventHitR[0]",
    "$SR1": "FootstepAnimEventHitR[1]",
    "$SR2": "FootstepAnimEventHitR[2]",
    "$SR3": "FootstepAnimEventHitR[3]",
    # Not seen in 6.0.1.18179 -- x is {E and B} , sequence time is taken of both, pivot of $STB. (Also, attachment info for attachment 0)
    "$STx": "Mount(?)",
    "$TRD": "HandleSpellEventSound",  # soundEffect ID is implicit by SpellRec
    "$VG0": "HandleBoneAnimGrabEvent[0]",
    "$VG1": "HandleBoneAnimGrabEvent[1]",
    "$VG2": "HandleBoneAnimGrabEvent[2]",
    "$VG3": "HandleBoneAnimGrabEvent[3]",
    "$VG4": "HandleBoneAnimGrabEvent[4]",
    "$VG5": "HandleBoneAnimGrabEvent[5]",
    "$VG6": "HandleBoneAnimGrabEvent[6]",
    "$VG7": "HandleBoneAnimGrabEvent[7]",
    "$VG8": "HandleBoneAnimGrabEvent[8]",
    "$VT0": "HandleBoneAnimThrowEvent[0]",
    "$VT1": "HandleBoneAnimThrowEvent[1]",
    "$VT2": "HandleBoneAnimThrowEvent[2]",
    "$VT3": "HandleBoneAnimThrowEvent[3]",
    "$VT4": "HandleBoneAnimThrowEvent[4]",
    "$VT5": "HandleBoneAnimThrowEvent[5]",
    "$VT6": "HandleBoneAnimThrowEvent[6]",
    "$VT7": "HandleBoneAnimThrowEvent[7]",
    "$VT8": "HandleBoneAnimThrowEvent[8]",
    # soundEffect ID is defined by CreatureSoundDataRec::m_soundWingGlideID
    "$WGG": "PlayUnitSound (wingGlide)",
    # soundEffect ID is defined by CreatureSoundDataRec::m_soundWingFlapID
    "$WNG": "PlayUnitSound (wingFlap)",
    "$WR0": "FootstepAnimEventHitL[0]",
    "$WR1": "FootstepAnimEventHitL[1]",
    "$WR2": "FootstepAnimEventHitL[2]",
    "$WR3": "FootstepAnimEventHitL[3]",
    "$WRB": "Bow Something",
    "$WRT": "Bow Something",
}


eventid_re = r"^/model/events/\d+/eventid$"


simplifiers: List[SimplifierUncompiled] = [
    (eventid_re, simplify_events),
]
