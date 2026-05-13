from geometry import Rectangle, Box, Placement
from utils import close
from constants import EPS


class AlgorithmA:

    def __init__(self):

        # Initially the whole unit square is empty
        self.boxes = [
            Box(0.0, 0.0, 1.0, 1.0)
        ]

        self.placements = []

    # ---------------------------------------------------------
    # Rectangle generator
    # ---------------------------------------------------------

    def rectangle(self, i: int) -> Rectangle:

        return Rectangle(
            index=i,
            width=1.0 / (i + 1),
            height=1.0 / i
        )

    # ---------------------------------------------------------
    # Check if rectangle fits
    # NO free rotation
    # ---------------------------------------------------------

    def fits(self, rect: Rectangle, box: Box) -> bool:

        return (
            rect.width <= box.w
            and
            rect.height <= box.h
        )

    # ---------------------------------------------------------
    # Choose smallest-width fitting box
    # ---------------------------------------------------------

    def choose_box(self, rect: Rectangle):

        fitting_boxes = []

        for b in self.boxes:

            if self.fits(rect, b):
                fitting_boxes.append(b)

        if len(fitting_boxes) == 0:
            return None

        fitting_boxes.sort(key=lambda b: (b.w, b.h))

        return fitting_boxes[0]

    # ---------------------------------------------------------
    # Remove box
    # ---------------------------------------------------------

    def remove_box(self, box: Box):

        self.boxes.remove(box)

    # ---------------------------------------------------------
    # Add valid box
    # ---------------------------------------------------------

    def add_box_if_valid(self, box: Box):

        if box.w > EPS and box.h > EPS:
            self.boxes.append(box)

    # ---------------------------------------------------------
    # Place rectangle
    # ---------------------------------------------------------

    def place(self, i: int):

        rect = self.rectangle(i)

        box = self.choose_box(rect)

        if box is None:
            print(f"FAILED at P_{i}")
            return False

        self.remove_box(box)

        rw = rect.width
        rh = rect.height

        # =====================================================
        # CASE 1
        # Exact fit
        # =====================================================

        if close(box.w, rw) and close(box.h, rh):

            self.placements.append(
                Placement(
                    i,
                    box.x,
                    box.y,
                    rw,
                    rh
                )
            )

            return True

        # =====================================================
        # CASE 2
        # Width matches exactly
        # =====================================================

        elif close(box.w, rw):

            self.placements.append(
                Placement(
                    i,
                    box.x,
                    box.y,
                    rw,
                    rh
                )
            )

            D = Box(
                box.x,
                box.y + rh,
                box.w,
                box.h - rh
            )

            self.add_box_if_valid(D)

            return True

        # =====================================================
        # CASE 3
        # General split
        # =====================================================

        else:

            self.placements.append(
                Placement(
                    i,
                    box.x,
                    box.y,
                    rw,
                    rh
                )
            )

            horizontal_leftover = box.w - rw
            vertical_leftover = box.h - rh

            # -------------------------------------------------
            # Subcase A
            # -------------------------------------------------

            if horizontal_leftover <= vertical_leftover:

                C = Box(
                    box.x + rw,
                    box.y,
                    box.w - rw,
                    rh
                )

                D = Box(
                    box.x,
                    box.y + rh,
                    box.w,
                    box.h - rh
                )

            # -------------------------------------------------
            # Subcase B
            # -------------------------------------------------

            else:

                C = Box(
                    box.x + rw,
                    box.y,
                    box.w - rw,
                    box.h
                )

                D = Box(
                    box.x,
                    box.y + rh,
                    rw,
                    box.h - rh
                )

            self.add_box_if_valid(C)
            self.add_box_if_valid(D)

            return True

    # ---------------------------------------------------------
    # Run algorithm
    # ---------------------------------------------------------

    def run(self, N: int):

        for i in range(1, N + 1):

            success = self.place(i)

            if not success:
                break

            if i % 100 == 0:
                print(f"Packed {i} rectangles")

    # ---------------------------------------------------------
    # Largest remaining square
    # ---------------------------------------------------------

    def largest_square_size(self):

        if len(self.boxes) == 0:
            return 0.0

        return max(
            min(b.w, b.h)
            for b in self.boxes
        )

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def statistics(self):

        print("--------------------------------")
        print(f"Placed rectangles : {len(self.placements)}")
        print(f"Remaining boxes   : {len(self.boxes)}")
        print(f"Largest square    : {self.largest_square_size()}")
        print("--------------------------------")