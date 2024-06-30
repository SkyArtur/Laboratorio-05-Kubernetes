FROM postgres:14
RUN localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV POSTGRES_DB=laboratorio
ENV POSTGRES_USER=estudante
ENV POSTGRES_PASSWORD=212223
ENV LANG pt_BR.utf8
EXPOSE 5432