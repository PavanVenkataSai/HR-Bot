tab1, tab2, tab3 = st.tabs(["Round_1", "Round_2", "Round_3"])

with tab1:
   @app.get('/Round_1')
    def Assesment_1(AptitudeQuestion: tuple[str, dict] = Depends(get_round_1_question),
                    Project_wise_queries: str = Depends(get_round_1_question)):

        if Fresher:
            string_content, dictionary_content = AptitudeQuestion

            return dictionary_content
        else:
            # Project_wise_queries = project_bot(raw_text)
            return Project_wise_queries

with tab2:
   @app.get("/Round_2")
    def Assesment_2(question: str = Depends(get_round_2_question)):

        if Fresher:
            return question
        else:
            return question

with tab3:
   @app.get('/Round_3')
    def Left_RightBrainValidation(L_R_Question: str = Depends(get_round_3_question)):
        return L_R_Question
