import wikipedia

class SearchService:

    def search(self, keyword):

        wikipedia.set_lang("en")

        try:
            print(f"[Wikipedia] Searching: {keyword}")

            results = wikipedia.search(keyword)
            print("[Wikipedia] Search results:", results)

            if not results:
                return None

            print("[Wikipedia] Fetching page:", results[0])

            page = wikipedia.page(
                results[0],
                auto_suggest=False
            )

            print("[Wikipedia] Fetching summary:", page.title)

            summary = wikipedia.summary(
                page.title,
                sentences=8,
                auto_suggest=False
            )

            print("[Wikipedia] Successfully retrieved:", page.title)

            return {
                "title": page.title,
                "body": summary,
                "url": page.url
            }

        except wikipedia.DisambiguationError as e:
            print("[Wikipedia] Disambiguation:", e.options[:5])
            return None

        except wikipedia.PageError as e:
            print("[Wikipedia] Page error:", repr(e))
            return None

        except Exception as e:
            print("[Wikipedia] Unexpected error:", repr(e))
            return None