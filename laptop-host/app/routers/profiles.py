from fastapi import APIRouter, Depends

from app.auth import require_session
from app.models.profile import Profile
from app.profile_service import profile_service

router = APIRouter(
    prefix="/profiles",
    tags=["Profiles"],
)


@router.get("")
def list_profiles(
    token: str = Depends(require_session),
):
    profiles = profile_service.load_profiles()

    return [
        {
            "id": profile.id,
            "name": profile.name,
        }
        for profile in profiles
    ]


@router.get("/{profile_id}")
def get_profile(
    profile_id: str,
    token: str = Depends(require_session),
):
    return profile_service.get_profile(profile_id)


@router.post("", response_model=Profile, status_code=201)
def create_profile(
    profile: Profile,
    token: str = Depends(require_session),
):
    return profile_service.create_profile(profile)


@router.put("/{profile_id}", response_model=Profile)
def update_profile(
    profile_id: str,
    profile: Profile,
    token: str = Depends(require_session),
):
    return profile_service.update_profile(profile_id, profile)


@router.delete("/{profile_id}", status_code=204)
def delete_profile(
    profile_id: str,
    token: str = Depends(require_session),
):
    profile_service.delete_profile(profile_id)
