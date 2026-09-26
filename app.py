# ============================================================
# KNOWLEDGE MAP
# ============================================================

elif st.session_state.page == "knowledge_map":

    if not st.session_state.diagnostic_complete:

        st.warning(
            "Complete the diagnostic first."
        )

    else:

        st.title("Your AI Knowledge Map")

        st.write(
            "Your scores are based on your performance "
            "in the diagnostic assessment."
        )

        st.divider()

        scores = st.session_state.domain_scores

        for subject in SUBJECTS:

            score = scores.get(subject)

            # ------------------------------------------------
            # COURSE / SUBJECT NAME
            # ------------------------------------------------

            st.markdown(
                f"<h2 style='margin-bottom: 5px;'>{subject}</h2>",
                unsafe_allow_html=True
            )

            # ------------------------------------------------
            # NOT ASSESSED
            # ------------------------------------------------

            if score is None:

                st.info("Not Assessed")

            # ------------------------------------------------
            # ASSESSED
            # ------------------------------------------------

            else:

                st.progress(score / 100)

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown(
                        "<div style='font-size: 15px; "
                        "font-weight: 600;'>Knowledge Score</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"<div style='font-size: 20px; "
                        f"font-weight: 500;'>{score}%</div>",
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        "<div style='font-size: 15px; "
                        "font-weight: 600;'>Status</div>",
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"<div style='font-size: 20px; "
                        f"font-weight: 500;'>{get_status(score)}</div>",
                        unsafe_allow_html=True
                    )

            st.write("")
            st.divider()

        # ----------------------------------------------------
        # RECOMMENDED STARTING POINT
        # ----------------------------------------------------

        assessed = {
            subject: score
            for subject, score in scores.items()
            if score is not None
        }

        if assessed:

            weakest_subject = min(
                assessed,
                key=assessed.get
            )

            weakest_score = assessed[
                weakest_subject
            ]

            st.markdown(
                "## Recommended Starting Point"
            )

            st.success(
                f"{weakest_subject} — {weakest_score}%"
            )

            if weakest_score < 40:

                st.write(
                    f"Your diagnostic indicates that you should "
                    f"build a strong foundation in {weakest_subject}."
                )

            elif weakest_score < 70:

                st.write(
                    f"You have some understanding of "
                    f"{weakest_subject}, but additional practice "
                    "will help strengthen your foundation."
                )

            elif weakest_score < 100:

                st.write(
                    f"You have a good foundation in "
                    f"{weakest_subject}. More practice can help "
                    "you progress further."
                )

            else:

                st.write(
                    f"You demonstrated strong performance in "
                    f"{weakest_subject}."
                )

        st.write("")

        if st.button(
            "View My Personalised Roadmap",
            use_container_width=True
        ):

            st.session_state.page = "roadmap"

            st.rerun()
