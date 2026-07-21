import wikipedia


class SearchService:

    def search(self, keyword):

        wikipedia.set_lang("en")

        try:

            # Search for similar pages first
            results = wikipedia.search(keyword)

            if not results:
                return None

            # Use the best matching result
            page = wikipedia.page(results[0], auto_suggest=False)

            summary = wikipedia.summary(page.title, sentences=8)

            return {
                "title": page.title,
                "body": summary,
                "url": page.url
            }

        except wikipedia.DisambiguationError as e:

            try:

                page = wikipedia.page(e.options[0], auto_suggest=False)

                summary = wikipedia.summary(page.title, sentences=8)

                return {
                    "title": page.title,
                    "body": summary,
                    "url": page.url
                }

            except Exception:
                return None

        except wikipedia.PageError:

            return None

        except Exception as e:

            print("Wikipedia Error:", e)

            return None