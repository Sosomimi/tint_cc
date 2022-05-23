from coding_challenge import DataCapture


def test_lenght_capture():
    capture = DataCapture()
    capture.add(1)
    capture.add(1)
    capture.add(2)

    assert len(capture.data) == 3


def test_case1():
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)

    stats = capture.build_stats()

    assert stats.less(4) == 2
    assert stats.between(3,6) == 4
    assert stats.greater(4) == 2


def test_case2():
    capture = DataCapture()
    for i in [9,7,6,5,5,5,4,4,3,2,1]:
        capture.add(i)

    stats = capture.build_stats()

    assert stats.less(3) == 2
    assert stats.less(5) == 5
    assert stats.less(7) == 9
    assert stats.greater(4) == 6
    assert stats.greater(3) == 8
    assert stats.greater(6) == 2
    assert stats.between(3,6) == 7
    assert stats.between(4,5) == 5
    assert stats.between(6,7) == 2


def test_case3():
    capture = DataCapture()
    for i in [8,9,8,2,1,6,7,3,8,11,2,7,5,5,5,8,9,12]:
        capture.add(i)

    stats = capture.build_stats()

    assert stats.less(6) == len([1, 2, 2, 3, 5, 5, 5])
    assert stats.greater(5) == len([6, 7, 7, 8, 8, 8, 8, 9, 9, 11, 12])
    assert stats.between(7,8) == len([7, 7, 8, 8, 8, 8])


def test_between_inverted():
    capture = DataCapture()
    for i in [9,7,6,5,5,5,4,4,3,2,1]:
        capture.add(i)

    stats = capture.build_stats()

    assert stats.between(6,3) == 7
    assert stats.between(5,4) == 5
    assert stats.between(7,6) == 2
