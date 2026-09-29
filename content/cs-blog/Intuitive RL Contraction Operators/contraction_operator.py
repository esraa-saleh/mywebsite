from manim import *
import numpy as np

# run this using : manim -pql contraction_operator.py ContractionOnLine

# ------------------------------------------------------------
# Helper contraction map:
# T(x) = p + beta (x - p)
# fixed point is p, contraction factor is beta (shown as \beta on screen)
# ------------------------------------------------------------

C = 0.6
P_FIXED_1D = 1.5
P_FIXED_2D = np.array([2.0, 1.0])

def T1(x):
    return P_FIXED_1D + C * (x - P_FIXED_1D)

def T2(point):
    point = np.array(point)
    return P_FIXED_2D + C * (point[:2] - P_FIXED_2D)


class ContractionOnLine(Scene):
    def construct(self):
        title = Tex("Contraction operator on a line").to_edge(UP)
        # Split into indexable pieces (this concatenates to the exact same
        # tex as before) so T(x), T(y), the standalone x/y and beta can each
        # be colored / pointed at independently. Note: T(x) and T(y) are
        # each kept as one whole piece rather than split further around
        # their argument -- isolating just the "x" glyph next to the "("
        # hits a dvisvgm glyph-merging quirk that produces a corrupted,
        # sliver-sized bounding box, so the arrow points at the whole
        # T(x)/T(y) term instead of just its argument.
        formula = MathTex(
            r"|", "T(x)", r"-", "T(y)", r"|", r"\le", r"\beta", r"\,|",
            "x", r"-", "y", r"|",
            r"\quad (0<", r"\beta", r"<1)",
        ).next_to(title, DOWN)
        tx_group = formula[1]
        ty_group = formula[3]
        formula_beta_main = formula[6]
        formula_x = formula[8]
        formula_y = formula[10]
        formula_beta_cond = formula[13]

        def pointer_arrow(start, end, color):
            return Arrow(
                start.get_bottom(), end.get_top(),
                buff=0.15, color=color, stroke_width=3,
                max_tip_length_to_length_ratio=0.12,
            )

        # Open with the general norm notation (double bars) rather than
        # jumping straight to absolute value, name the specific norm being
        # used, then swap to the single-bar formula everything below
        # actually operates on. Fade out/in, not Transform -- morphing
        # double bars into single bars glyph-by-glyph is exactly the kind
        # of mismatched-shape morph that renders as an illegible blob
        # elsewhere in this scene.
        formula_norm = MathTex(
            r"\|", "T(x)", r"-", "T(y)", r"\|", r"\le", r"\beta", r"\,\|",
            "x", r"-", "y", r"\|",
            r"\quad (0<", r"\beta", r"<1)",
        ).next_to(title, DOWN)

        self.play(Write(title), Write(formula_norm))
        self.wait(1.0)

        norm_note = Tex(r"Using the $p=1$ norm: absolute value").scale(0.6)
        norm_note.next_to(formula_norm, DOWN, buff=0.3)
        self.play(FadeIn(norm_note))
        self.wait(1.3)

        self.play(FadeOut(norm_note), FadeOut(formula_norm))
        self.play(FadeIn(formula))
        self.wait(1.4)

        # Before anything else: make sure the viewer clocks that T(x) and
        # T(y) are just T applied to the x and y sitting on the other side
        # of the inequality -- box the standalone x/y, box the whole T(x)/
        # T(y) term, and link them with a curved arrow. One pair at a time
        # so it reads as "this x" -> "that's what T(x) means".
        box_x_rhs = SurroundingRectangle(formula_x, color=BLUE, buff=0.08)
        box_Tx = SurroundingRectangle(tx_group, color=BLUE, buff=0.08)
        link_x = CurvedArrow(
            box_x_rhs.get_bottom(), box_Tx.get_bottom(),
            color=BLUE, angle=-TAU / 4, stroke_width=3,
        )
        self.play(Create(box_x_rhs), run_time=1.2)
        self.wait(0.5)
        self.play(Create(box_Tx), Create(link_x), run_time=1.2)
        self.wait(1.1)
        self.play(FadeOut(box_x_rhs), FadeOut(box_Tx), FadeOut(link_x))

        box_y_rhs = SurroundingRectangle(formula_y, color=YELLOW, buff=0.08)
        box_Ty = SurroundingRectangle(ty_group, color=YELLOW, buff=0.08)
        link_y = CurvedArrow(
            box_y_rhs.get_bottom(), box_Ty.get_bottom(),
            color=YELLOW, angle=-TAU / 4, stroke_width=3,
        )
        self.play(Create(box_y_rhs), run_time=1.2)
        self.wait(0.5)
        self.play(Create(box_Ty), Create(link_y), run_time=1.2)
        self.wait(1.1)
        self.play(FadeOut(box_y_rhs), FadeOut(box_Ty), FadeOut(link_y))
        self.wait(0.5)

        x_val = -2.0
        y_val = 4.0
        tx_val = T1(x_val)
        ty_val = T1(y_val)

        def make_line(y_shift):
            nl = NumberLine(x_range=[-4, 6, 1], length=10, include_numbers=True)
            nl.shift(UP * y_shift)
            return nl

        # ============================================================
        # Line 1 -- the specific example. x and y appear, then the
        # *same* segment scales down in place toward the fixed point:
        # T(x) = p + beta*(x-p) is literally "scale by beta about p",
        # so there's nothing to copy anywhere -- just watch it shrink.
        # ============================================================
        line1 = make_line(0.8)
        self.play(Create(line1))

        x_dot = Dot(line1.n2p(x_val), color=BLUE)
        y_dot = Dot(line1.n2p(y_val), color=YELLOW)

        arrow_x = pointer_arrow(formula_x, x_dot, BLUE)
        arrow_y = pointer_arrow(formula_y, y_dot, YELLOW)
        self.play(GrowArrow(arrow_x), GrowArrow(arrow_y), run_time=1.2)
        self.wait(0.7)
        self.play(FadeOut(arrow_x), FadeOut(arrow_y))

        x_label = MathTex("x", color=BLUE).scale(0.7).next_to(x_dot, UP, buff=0.25)
        y_label = MathTex("y", color=YELLOW).scale(0.7).next_to(y_dot, UP, buff=0.25)
        self.play(
            FadeIn(x_dot), FadeIn(y_dot), FadeIn(x_label), FadeIn(y_label),
            formula_x.animate.set_color(BLUE),
            formula_y.animate.set_color(YELLOW),
        )

        # x and y stay put right here for the rest of the scene -- this
        # segment is a fixed, permanent reference labeled "d", symbol
        # only, no number: it never changes, so there's nothing to count.
        segment1 = Line(line1.n2p(x_val), line1.n2p(y_val), color=WHITE, stroke_width=6)
        dist1_label = MathTex("d").scale(0.7)
        dist1_label.next_to(segment1, UP, buff=0.5)
        self.play(Create(segment1), FadeIn(dist1_label))
        self.wait(1.2)

        # A *second*, unlabeled pair starts right on top of x and y and
        # contracts toward the fixed point -- x, y and the "d" segment
        # never move again. Green from the start, so even while it's
        # sitting exactly on top of the white segment it reads as a
        # distinct thing, and as it contracts the white "d" segment
        # reappears from underneath on both sides.
        progress = ValueTracker(0.0)

        def interp(a, b):
            return a + progress.get_value() * (b - a)

        c1_dot = Dot(line1.n2p(x_val), color=GREEN)
        c2_dot = Dot(line1.n2p(y_val), color=GREEN)
        c1_dot.add_updater(lambda m: m.move_to(line1.n2p(interp(x_val, tx_val))))
        c2_dot.add_updater(lambda m: m.move_to(line1.n2p(interp(y_val, ty_val))))

        seg_contract = Line(line1.n2p(x_val), line1.n2p(y_val), color=GREEN, stroke_width=6)
        seg_contract.add_updater(
            lambda m: m.put_start_and_end_on(c1_dot.get_center(), c2_dot.get_center())
        )

        self.play(FadeIn(c1_dot), FadeIn(c2_dot), Create(seg_contract))

        # "d" only ever meant the fixed x-to-y gap; once it's actually
        # shrinking there's no single "d" being described anymore, so
        # drop the label rather than leave a stale name sitting there.
        self.play(FadeOut(dist1_label))

        self.play(progress.animate.set_value(1.0), run_time=4.5, rate_func=smooth)
        self.wait(0.8)

        for mobj in (c1_dot, c2_dot, seg_contract):
            mobj.clear_updaters()

        # Label the settled segment beta*d -- symbol only, no number here
        # either -- with a pointer arrow down from beta in the equation.
        # "d" is already gone by now, so this can sit right above the
        # segment instead of reserving a separate lane for both.
        beta_d_label = MathTex(r"\beta\,d", color=GREEN).scale(0.7)
        beta_d_label.next_to(seg_contract, UP, buff=0.5)

        arrow_beta = pointer_arrow(formula_beta_main, beta_d_label, GREEN)
        self.play(GrowArrow(arrow_beta), run_time=1.2)
        self.wait(0.7)
        self.play(FadeOut(arrow_beta))

        self.play(
            FadeIn(beta_d_label),
            formula_beta_main.animate.set_color(GREEN),
            formula_beta_cond.animate.set_color(GREEN),
        )
        self.wait(1.3)

        d_original = abs(y_val - x_val)

        # Spell out what a claimed beta actually means, right on line 1 --
        # a translucent highlight of length claim_beta*d, anchored at the
        # same left edge (tx_val) line 1's own result starts from -- then
        # this physical object gets carried down to line 2 in a moment,
        # rather than a fresh rectangle conjured there with no visible
        # connection back to where the length came from. Reused for both
        # the true claim and the wrong one below.
        def make_line1_claim(claim_beta, start_length=None):
            label = Tex(f"Let $\\beta = {claim_beta}$").scale(0.55)
            label.next_to(line1, DOWN, buff=0.3).align_to(line1, LEFT)
            self.play(FadeIn(label))

            length = claim_beta * d_original
            # First claim has nothing to shrink *from* yet, so it just
            # appears at its own length. The second claim starts at the
            # *first* claim's actual length and visibly shrinks down to
            # its own, shorter one -- a real before/after, not an
            # arbitrarily oversized rectangle starting past y for no reason.
            initial_length = start_length if start_length is not None else length
            hl = Rectangle(
                width=initial_length, height=0.5, stroke_width=2, stroke_color=GREEN,
                stroke_opacity=0.9, fill_color=GREEN, fill_opacity=0.4,
            )
            hl.move_to(line1.n2p(tx_val + initial_length / 2))
            hl.set_z_index(-1)
            self.play(FadeIn(hl))
            if start_length is not None:
                self.wait(0.4)
                # The solid beta*d segment and its label shrink right along
                # with the highlight -- this line now shows the *current*
                # claimed beta, not just the (still-true) original 0.6.
                # Driven by explicit updaters (the pattern already proven
                # reliable elsewhere in this scene), not bundled .animate
                # calls -- those turned out to silently break seg_contract's
                # rendering when run alongside the z-indexed highlight.
                shrink_progress = ValueTracker(0.0)
                label_y = beta_d_label.get_y()

                def current_len():
                    return initial_length + shrink_progress.get_value() * (
                        length - initial_length
                    )

                def update_hl(m):
                    w = current_len()
                    m.stretch_to_fit_width(w)
                    m.move_to(line1.n2p(tx_val + w / 2))

                def update_seg(m):
                    m.put_start_and_end_on(
                        line1.n2p(tx_val), line1.n2p(tx_val + current_len())
                    )

                def update_c2(m):
                    m.move_to(line1.n2p(tx_val + current_len()))

                def update_label(m):
                    x = line1.n2p(tx_val + current_len() / 2)[0]
                    m.move_to([x, label_y, 0])

                hl.add_updater(update_hl)
                seg_contract.add_updater(update_seg)
                c2_dot.add_updater(update_c2)
                beta_d_label.add_updater(update_label)
                self.play(shrink_progress.animate.set_value(1.0), run_time=1.2)
                hl.clear_updaters()
                seg_contract.clear_updaters()
                c2_dot.clear_updaters()
                beta_d_label.clear_updaters()
            self.wait(0.6)
            # Stays on screen -- test_claim below boxes it in red rather
            # than restating "Let beta = ..." a second time near line 2.
            return hl, label

        highlight1, label1 = make_line1_claim(C)

        # ============================================================
        # Line 2 -- check a *claimed* contraction constant against one
        # fixed pair, by measuring. A genuine T(x), T(y) that violates
        # the true beta can't exist for this map (it's affine, so the
        # inequality is always exact equality) -- so what varies between
        # rounds isn't the pair, it's the claim being tested: the real
        # beta=0.6 (holds), then a wrong, too-tight guess like beta=0.3
        # (fails, since this T never shrinks anything that much).
        # ============================================================
        line2 = make_line(-1.8)
        self.play(Create(line2))

        # A pair shifted well away from line 1's own T(x), T(y), with a
        # *larger* gap than before (4 instead of 3) -- chosen so that the
        # true claim still lands with room to spare, but the wrong claim
        # (measured the same way, against line 1's own d) now genuinely
        # falls short too, rather than landing on it by coincidence.
        xp, yp = -3.0, 1.0
        txp, typ = T1(xp), T1(yp)
        gap_p = abs(yp - xp)

        p_dot = Dot(line2.n2p(txp), color=BLUE)
        q_dot = Dot(line2.n2p(typ), color=YELLOW)

        # Point down from the equation's own T(x), T(y) *before* this new
        # pair appears -- same "explanation before the visual" rule used
        # everywhere else in this scene -- then color those terms to match
        # once the pair actually lands.
        arrow_p = pointer_arrow(tx_group, p_dot, BLUE)
        arrow_q = pointer_arrow(ty_group, q_dot, YELLOW)
        self.play(GrowArrow(arrow_p), GrowArrow(arrow_q), run_time=1.2)
        self.wait(0.7)
        self.play(FadeOut(arrow_p), FadeOut(arrow_q))

        p_label = MathTex("T(x)", color=BLUE).scale(0.6).next_to(p_dot, UP, buff=0.25)
        q_label = MathTex("T(y)", color=YELLOW).scale(0.6).next_to(q_dot, UP, buff=0.25)
        seg = Line(line2.n2p(txp), line2.n2p(typ), color=WHITE, stroke_width=6)
        self.play(
            FadeIn(p_dot), FadeIn(q_dot), FadeIn(p_label), FadeIn(q_label), Create(seg),
            tx_group.animate.set_color(BLUE),
            ty_group.animate.set_color(YELLOW),
        )
        self.wait(0.6)

        def make_check(color):
            m = VMobject(color=color, stroke_width=8)
            m.set_points_as_corners([LEFT * 0.18, DOWN * 0.12, RIGHT * 0.32 + UP * 0.35])
            return m

        def make_cross(color):
            l1 = Line(UL * 0.22, DR * 0.22, color=color, stroke_width=8)
            l2 = Line(UR * 0.22, DL * 0.22, color=color, stroke_width=8)
            return VGroup(l1, l2)

        def test_claim(highlight, label):
            # highlight's width is already claim_beta*d (built by
            # make_line1_claim above) -- valid iff that reaches at least
            # as far as this pair's actual result, beta*gap_p.
            ruler_len = highlight.width
            valid = ruler_len >= C * gap_p - 1e-9

            # No need to restate "Let beta = ..." down here -- it's already
            # sitting next to line 1. Just box it in red to mark it as the
            # claim currently being tested.
            box = SurroundingRectangle(label, color=RED, buff=0.08)
            self.play(Create(box))

            # Carry the highlight physically down from line 1 and lay its
            # left edge on T(x) -- not a fresh rectangle conjured here with
            # no visible link to where that length came from.
            self.play(
                highlight.animate.move_to(line2.n2p(txp + ruler_len / 2)), run_time=1.5
            )
            self.wait(0.6)

            color = GREEN if valid else RED
            mark = make_check(color) if valid else make_cross(color)
            verdict_text = Tex(
                "Inequality satisfied" if valid else "Inequality not satisfied",
                color=color,
            ).scale(0.7)
            verdict = VGroup(mark, verdict_text).arrange(RIGHT, buff=0.3)
            verdict.next_to(line2, DOWN, buff=0.6)

            self.play(seg.animate.set_color(color), Write(verdict_text), FadeIn(mark))
            self.wait(1.5)

            self.play(FadeOut(box), FadeOut(label), FadeOut(highlight), FadeOut(verdict))
            seg.set_color(WHITE)

        # Round 1: the true beta -- this pair started closer together than
        # line 1's own pair, so the carried highlight lands with room to
        # spare: |T(x)-T(y)| strictly less than beta*d, not just equal.
        test_claim(highlight1, label1)

        # Round 2: back to line 1 for the *same* flow with a wrong, too
        # tight claim -- starting at the first claim's actual length and
        # shrinking down to this shorter one, which falls short of T(y)
        # once carried down. This T only ever guarantees shrinking by a
        # factor of C, never more.
        highlight2, label2 = make_line1_claim(0.3, start_length=C * d_original)
        test_claim(highlight2, label2)

        self.play(
            FadeOut(p_dot), FadeOut(q_dot), FadeOut(p_label), FadeOut(q_label), FadeOut(seg),
            tx_group.animate.set_color(WHITE),
            ty_group.animate.set_color(WHITE),
        )

        conclusion = Tex(
            "As long as ", "$T(x)$", " and ", "$T(y)$",
            " are less than or equal to ", r"$\beta\,d$",
            " apart, then ", "$T$", " is a contraction",
        ).scale(0.6)
        conclusion[1].set_color(BLUE)
        conclusion[3].set_color(YELLOW)
        conclusion[5].set_color(GREEN)
        conclusion.next_to(line2, DOWN, buff=0.6)
        self.play(Write(conclusion))
        self.wait(2.5)


class ContractionCloud(Scene):
    def construct(self):
        title = Tex("A contraction shrinks an entire cloud of points").to_edge(UP)
        formula = MathTex(
            r"\|T(u)-T(v)\| \le \beta\|u-v\|"
        ).next_to(title, DOWN)

        self.play(Write(title), Write(formula))
        self.wait(1)

        plane = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-2, 4, 1],
            background_line_style={
                "stroke_opacity": 0.35,
                "stroke_width": 1,
            },
        ).scale(0.9).shift(DOWN * 0.3)

        self.play(Create(plane))

        fp = Dot(plane.c2p(*P_FIXED_2D), color=RED)
        fp_label = MathTex("x^*", color=RED).scale(0.8).next_to(fp, UR, buff=0.15)
        self.play(FadeIn(fp), FadeIn(fp_label))

        points = [
            np.array([-0.5, 2.6]),
            np.array([0.2, 0.4]),
            np.array([1.1, 3.0]),
            np.array([3.8, -0.5]),
            np.array([4.2, 2.5]),
            np.array([2.9, 3.2]),
            np.array([0.8, -1.0]),
        ]

        dots = VGroup()
        image_dots = VGroup()
        arrows = VGroup()

        for p in points:
            q = T2(p)
            d = Dot(plane.c2p(*p), radius=0.07, color=BLUE)
            dq = Dot(plane.c2p(*q), radius=0.07, color=GREEN)
            a = Arrow(
                plane.c2p(*p),
                plane.c2p(*q),
                buff=0.05,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15,
                color=GRAY_B,
            )
            dots.add(d)
            image_dots.add(dq)
            arrows.add(a)

        self.play(FadeIn(dots))
        self.wait(1)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1))
        self.play(FadeIn(image_dots))
        self.wait(1)

        cloud_text = Tex("Every point moves closer to the fixed point").scale(0.8)
        cloud_text.next_to(plane, DOWN)
        self.play(Write(cloud_text))
        self.wait(2)


class FixedPointIteration(Scene):
    def construct(self):
        title = Tex("Repeated application converges to a fixed point").to_edge(UP)
        equation = MathTex(
            r"x_{n+1}=T(x_n), \qquad T(x^*)=x^*"
        ).next_to(title, DOWN)

        self.play(Write(title), Write(equation))
        self.wait(1)

        plane = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-2, 4, 1],
            background_line_style={
                "stroke_opacity": 0.35,
                "stroke_width": 1,
            },
        ).scale(0.9).shift(DOWN * 0.3)

        self.play(Create(plane))

        fp = Dot(plane.c2p(*P_FIXED_2D), color=RED)
        fp_label = MathTex("x^*", color=RED).scale(0.8).next_to(fp, UR, buff=0.15)

        self.play(FadeIn(fp), FadeIn(fp_label))

        x0 = np.array([4.3, 3.3])
        orbit = [x0]
        for _ in range(6):
            orbit.append(T2(orbit[-1]))

        dots = VGroup()
        labels = VGroup()
        arrows = VGroup()

        for i, p in enumerate(orbit):
            d = Dot(plane.c2p(*p), radius=0.07, color=BLUE if i == 0 else GREEN)
            lab = MathTex(f"x_{i}").scale(0.7).next_to(d, UR, buff=0.08)
            dots.add(d)
            labels.add(lab)

        for i in range(len(orbit) - 1):
            a = Arrow(
                plane.c2p(*orbit[i]),
                plane.c2p(*orbit[i + 1]),
                buff=0.05,
                color=YELLOW,
                stroke_width=3,
                max_tip_length_to_length_ratio=0.15,
            )
            arrows.add(a)

        self.play(FadeIn(dots[0]), FadeIn(labels[0]))
        self.wait(0.5)

        for i in range(len(arrows)):
            self.play(
                GrowArrow(arrows[i]),
                FadeIn(dots[i + 1]),
                FadeIn(labels[i + 1]),
                run_time=0.8,
            )

        self.wait(1)

        conclusion = Tex("The iterates get pulled into the fixed point").scale(0.8)
        conclusion.next_to(plane, DOWN)
        self.play(Write(conclusion))
        self.wait(2)