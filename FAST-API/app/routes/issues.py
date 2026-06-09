import uuid

from fastapi import APIRouter, HTTPException, status

from app.schemas import (
    IssueCreate,
    IssueOut,
    IssueUpdate,
    IssueStatus,
)

from app.storage import load_data, save_data


router = APIRouter(
    prefix="/api/v1/issues",
    tags=["Issues"]
)


@router.get("/", response_model=list[IssueOut])
async def get_issues():
    """
    Retrieve all issues.
    """
    return load_data()


@router.get("/{issue_id}", response_model=IssueOut)
async def get_issue(issue_id: str):
    """
    Retrieve a single issue.
    """
    issues = load_data()

    for issue in issues:
        if issue["id"] == issue_id:
            return issue

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )


@router.post(
    "/",
    response_model=IssueOut,
    status_code=status.HTTP_201_CREATED
)
async def create_issue(payload: IssueCreate):
    """
    Create a new issue.
    """
    issues = load_data()

    new_issue = {
        "id": str(uuid.uuid4()),
        "title": payload.title,
        "description": payload.description,
        "priority": payload.priority.value,
        "status": IssueStatus.open.value,
    }

    issues.append(new_issue)
    save_data(issues)

    return new_issue


@router.put("/{issue_id}", response_model=IssueOut)
async def update_issue(issue_id: str, payload: IssueUpdate):
    """
    Update an existing issue.
    """
    issues = load_data()

    for issue in issues:
        if issue["id"] == issue_id:

            if payload.title is not None:
                issue["title"] = payload.title

            if payload.description is not None:
                issue["description"] = payload.description

            if payload.priority is not None:
                issue["priority"] = payload.priority.value

            if payload.status is not None:
                issue["status"] = payload.status.value

            save_data(issues)
            return issue

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )


@router.delete("/{issue_id}")
async def delete_issue(issue_id: str):
    """
    Delete an issue.
    """
    issues = load_data()

    for issue in issues:
        if issue["id"] == issue_id:
            issues.remove(issue)
            save_data(issues)

            return {
                "message": "Issue deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Issue not found"
    )