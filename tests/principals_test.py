from core.models.assignments import AssignmentStateEnum, GradeEnum


def test_get_assignments(client, h_principal):
    response = client.get(
        '/principal/assignments',
        headers=h_principal
    )

    assert response.status_code == 200

    data = response.json['data']
    for assignment in data:
        assert assignment['state'] in [AssignmentStateEnum.SUBMITTED, AssignmentStateEnum.GRADED]


def test_grade_assignment_draft_assignment(client, h_principal):
    """
    failure case: If an assignment is in Draft state, it cannot be graded by principal
    """
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 5,
            'grade': GradeEnum.A.value
        },
        headers=h_principal
    )

    assert response.status_code == 400


def test_grade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.C


def test_regrade_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 4,
            'grade': GradeEnum.B.value
        },
        headers=h_principal
    )

    assert response.status_code == 200

    assert response.json['data']['state'] == AssignmentStateEnum.GRADED.value
    assert response.json['data']['grade'] == GradeEnum.B


def test_grade_missing_assignment(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'id': 100,
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )
    assert response.status_code == 404

def test_grade_assignment_without_id(client, h_principal):
    response = client.post(
        '/principal/assignments/grade',
        json={
            'grade': GradeEnum.C.value
        },
        headers=h_principal
    )
    assert response.status_code == 400

def test_get_teacher_list(client, h_principal):
    response = client.get(
        '/principal/teachers',
        headers=h_principal
    )
    assert response.status_code == 200
    data = response.json['data']
    expected_result = [
        {'id': 1, 'user_id': 3},
        {'id': 2, 'user_id': 4}
    ]
    
    actual_result = [
        {'id': teacher['id'], 'user_id': teacher['user_id']} for teacher in data
    ]

    assert expected_result == actual_result


