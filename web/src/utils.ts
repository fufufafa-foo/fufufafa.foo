import readme from "../../readme.md?raw";

const LINE_OFFSET = 5;
const readmeLines = readme.split("\n");

export interface Content {
  id: string;
  title: string;
  img: string;
  link?: string;
}

export const findArchiveLink = (title: string) => {
  const index = readmeLines.findIndex((line) => line.includes(title));
  if (index === -1) return;

  const link = readmeLines[index + LINE_OFFSET];
  if (!link.startsWith("https://")) return;

  return link;
};

export const parseContents = (): Content[] => {
  const REGEX = /^##\s+\d+\.\s+(.*)/gm;

  const matches = readme.match(REGEX);
  if (!matches) return [];

  return matches.map((match: string): Content => {
    const id = match.substring(4, 7);
    const title = match.substring(9).trim();
    const img = `img/${id}.png`;
    const link = findArchiveLink(match);
    return { id, title, img, link };
  });
};

export const filterContent = (keyword: string) => {
  return ({ title }: Content) => {
    return title.toLowerCase().includes(keyword.toLowerCase());
  };
};
